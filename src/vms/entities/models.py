from datetime import datetime, timedelta
import uuid

from django.core.validators import RegexValidator
from django.db import models
from django.db.models import F, Q
from django.utils.timezone import localtime

PHONE_REGEX = RegexValidator(
    regex=r"^0\d{3}\s\d{3}\s\d{3}$",
    message="Telephone number must be entered in the format '0XXX XXX XXX'"
)
PHONE_FORMAT = "Format: '0XXX XXX XXX'"


class CID(models.Model):
    cid = models.UUIDField(default=uuid.uuid4, editable=False, verbose_name="Content ID",
                           help_text="Unique identifier", db_index=True)

    class Meta:
        abstract = True


class Location(CID, models.Model):
    name = models.CharField(max_length=127, verbose_name="Location name")
    internal_id = models.IntegerField(null=True, blank=True)

    manager_name = models.CharField(max_length=127, verbose_name="Manager name")
    manager_phone = models.CharField(max_length=50, verbose_name="Manager phone",
                                     validators=[PHONE_REGEX, ], help_text=PHONE_FORMAT)

    assistant_1_name = models.CharField(null=True, blank=True,
                                        max_length=127, verbose_name="Assistant name")
    assistant_1_phone = models.CharField(null=True, blank=True,
                                         max_length=50, verbose_name="Assistant phone",
                                         validators=[PHONE_REGEX, ], help_text=PHONE_FORMAT)

    assistant_2_name = models.CharField(null=True, blank=True,
                                        max_length=127, verbose_name="Assistant 2 name")
    assistant_2_phone = models.CharField(null=True, blank=True,
                                         max_length=50, verbose_name="Assistant phone",
                                         validators=[PHONE_REGEX, ], help_text=PHONE_FORMAT)

    laptop_sn = models.CharField(null=True, blank=True,
                                 max_length=10, verbose_name="Laptop serial number")

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        ordering = ['internal_id']


class Movie(CID, models.Model):
    original_title = models.CharField(max_length=127)
    english_title = models.CharField(max_length=127)
    romanian_title = models.CharField(max_length=127)
    duration = models.DurationField(verbose_name="Duration (minutes)",
                                    help_text="Movie duration in minutes.")
    format = models.CharField(null=True, blank=True, max_length=10,
                              choices=(
                                  ('dcp', "DCP"),
                                  ('35', "35mm"),
                                  ('digital', "Digital"),
                              ))
    over18 = models.BooleanField(default=False, verbose_name="Over 18",
                                 help_text="Is the movie rated R?")
    spoken_language_1 = models.CharField(null=True, blank=True, max_length=127)
    spoken_language_2 = models.CharField(null=True, blank=True, max_length=127)
    original_subtitle = models.CharField(null=True, blank=True, max_length=127)

    electronic_sub_1_language = models.CharField(null=True, blank=True, max_length=127,
                                                 verbose_name="Electronic subtitle 1 language")
    electronic_sub_1_format = models.CharField(null=True, blank=True, max_length=127,
                                               verbose_name="Electronic subtitle 1 format")
    electronic_sub_2_language = models.CharField(null=True, blank=True, max_length=127,
                                                 verbose_name="Electronic subtitle 2 language")
    electronic_sub_2_format = models.CharField(null=True, blank=True, max_length=127,
                                               verbose_name="Electronic subtitle 2 format")

    def __str__(self):
        return "{} ({})".format(self.romanian_title, self.duration)


class Volunteer(CID, models.Model):
    name = models.CharField(max_length=127, verbose_name="Volunteer name")
    email = models.CharField(max_length=127, verbose_name="Volunteer e-mail address")
    age = models.PositiveIntegerField()
    phone_1 = models.CharField(max_length=50, validators=[PHONE_REGEX, ], help_text=PHONE_FORMAT)
    phone_2 = models.CharField(null=True, blank=True,
                               max_length=50, validators=[PHONE_REGEX, ], help_text=PHONE_FORMAT)
    language_1 = models.CharField(null=True, blank=True, max_length=127)
    language_2 = models.CharField(null=True, blank=True, max_length=127)
    language_3 = models.CharField(null=True, blank=True, max_length=127)
    language_4 = models.CharField(null=True, blank=True, max_length=127)

    def __str__(self):
        return "{}".format(self.name)

    @property
    def schedule(self):
        return (self.schedule_1.all() | self.schedule_2.all()).distinct()


class Projection(CID, models.Model):
    date = models.DateTimeField()
    location = models.ForeignKey('Location')
    movie = models.ForeignKey('Movie')
    two_volunteers = models.BooleanField(default=False, help_text="Needs two volunteers?")
    special_notes = models.CharField(null=True, blank=True, max_length=255)

    def __str__(self):
        return "{} {}: {} - {}".format(self.day, self.hour, self.location, self.movie)

    class Meta:
        ordering = ['date']

    def _set_date(self, new_date, commit=True):
        self.date = new_date
        commit and self.save()

    @property
    def day(self):
        return localtime(self.date).strftime("%d %b %Y")

    @property
    def hour(self):
        return localtime(self.date).strftime("%H:%M")


class Availability(CID, models.Model):
    DAYS = [
        (2, "2 iunie"),
        (3, "3 iunie"),
        (4, "4 iunie"),
        (5, "5 iunie"),
        (6, "6 iunie"),
        (7, "7 iunie"),
        (8, "8 iunie"),
        (9, "9 iunie"),
        (10, "10 iunie"),
        (11, "11 iunie"),
    ]
    day = models.IntegerField(choices=DAYS)
    start = models.TimeField()
    end = models.TimeField()
    volunteer = models.ForeignKey('Volunteer')

    class Meta:
        verbose_name_plural = "Availabilities"


class ScheduleQuerySet(models.query.QuerySet):
    def current(self):
        start = localtime() - timedelta(minutes=10) - F('projection__movie__duration')
        end = localtime() + timedelta(minutes=15)
        q = Q(projection__date__gte=start) & Q(projection__date__lte=end)
        return self.filter(q)


class VolunteerSchedule(CID, models.Model):
    projection = models.ForeignKey(
        'Projection', related_name='schedule',
        limit_choices_to={'date__gte': datetime(year=datetime.now().year,
                                                month=datetime.now().month,
                                                day=datetime.now().day)}
    )
    volunteer_1 = models.ForeignKey('Volunteer', related_name='schedule_1')
    volunteer_2 = models.ForeignKey('Volunteer', null=True, blank=True, related_name='schedule_2')

    objects = ScheduleQuerySet.as_manager()

    def __str__(self):
        return "{}: {}, {}".format(self.projection, self.volunteer_1, self.volunteer_2)


class Laptop(models.Model):
    pass
