from datetime import timedelta

from django.core.validators import RegexValidator
from django.db import models
from django.utils.timezone import localtime, now

telephone_regex = RegexValidator(
        regex=r"^0\d{3}\s\d{3}\s\d{3}$",
        message=("Telephone number must be entered in the format "
                 "'0XXX XXX XXX'")
    )


class Location(models.Model):
    name = models.CharField(
        max_length=127,
        verbose_name="Location name",
    )

    manager_name = models.CharField(
        max_length=127,
        verbose_name="Manager name",
    )

    manager_phone = models.CharField(
        max_length=50,
        validators=[telephone_regex, ],
        verbose_name="Manager phone",
        help_text="Format: '0XXX XXX XXX'",
    )

    assistant_1_name = models.CharField(
        null=True, blank=True,
        max_length=127,
        verbose_name="Assistant name",
    )

    assistant_1_phone = models.CharField(
        null=True, blank=True,
        max_length=50,
        validators=[telephone_regex, ],
        verbose_name="Assistant phone",
        help_text="Format: '0XXX XXX XXX'",
    )

    assistant_2_name = models.CharField(
        null=True, blank=True,
        max_length=127,
        verbose_name="Assistant name",
    )

    assistant_2_phone = models.CharField(
        null=True, blank=True,
        max_length=50,
        validators=[telephone_regex, ],
        verbose_name="Assistant phone",
        help_text="Format: '0XXX XXX XXX'",
    )

    laptop_sn = models.CharField(
        null=True, blank=True,
        max_length=10,
        verbose_name="Laptop serial number",
    )
    internal_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        ordering = ['internal_id']


class Movie(models.Model):
    original_title = models.CharField(max_length=127)
    english_title = models.CharField(max_length=127)
    romanian_title = models.CharField(max_length=127)
    duration = models.PositiveIntegerField(
        null=True, blank=True,
        verbose_name="Duration (minutes)",
        help_text="Movie duration in minutes.",
    )
    format = models.CharField(
        null=True, blank=True,
        max_length=10,
        choices=(
            ('dcp', "DCP"),
            ('35', "35mm"),
            ('digital', "Digital"),
        ),
    )
    over18 = models.BooleanField(
        default=False,
        verbose_name="Over 18",
        help_text="Is the movie rated R?",
    )

    spoken_language_1 = models.CharField(
        null=True, blank=True,
        max_length=127,
    )
    spoken_language_2 = models.CharField(
        null=True, blank=True,
        max_length=127,
    )

    original_subtitle = models.CharField(
        null=True, blank=True,
        max_length=127,
    )
    electronic_sub_1_language = models.CharField(
        null=True, blank=True,
        max_length=127,
        verbose_name="Electronic subtitle 1 language",
    )
    electronic_sub_1_format = models.CharField(
        null=True, blank=True,
        max_length=127,
        verbose_name="Electronic subtitle 1 format",
    )
    electronic_sub_2_language = models.CharField(
        null=True, blank=True,
        max_length=127,
        verbose_name="Electronic subtitle 2 language",
    )
    electronic_sub_2_format = models.CharField(
        null=True, blank=True,
        max_length=127,
        verbose_name="Electronic subtitle 2 format",
    )

    def __str__(self):
        return "{} ({})".format(self.romanian_title, self.duration)


class Volunteer(models.Model):
    name = models.CharField(
        max_length=127,
        verbose_name="Volunteer name",
    )
    email = models.CharField(
        max_length=127,
        verbose_name="Volunteer e-mail address",
    )
    age = models.PositiveIntegerField()
    phone_1 = models.CharField(
        max_length=50,
        validators=[telephone_regex, ],
        help_text="Format: '0XXX XXX XXX'",
    )
    phone_2 = models.CharField(
        null=True, blank=True,
        max_length=50,
        validators=[telephone_regex, ],
        help_text="Format: '0XXX XXX XXX'",
    )
    language_1 = models.CharField(max_length=127, null=True, blank=True)
    language_2 = models.CharField(max_length=127, null=True, blank=True)
    language_3 = models.CharField(max_length=127, null=True, blank=True)
    language_4 = models.CharField(max_length=127, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class Projection(models.Model):
    date = models.DateTimeField()
    location = models.ForeignKey('Location')
    movie = models.ForeignKey('Movie')
    two_volunteers = models.BooleanField(
        default=False,
        help_text="Needs two volunteers?",
    )
    special_notes = models.CharField(
        null=True, blank=True,
        max_length=255,
    )

    def __str__(self):
        return "{}: {} - {}".format(localtime(self.date), self.location,
                                    self.movie)

    class Meta:
        ordering = ['date']


class Availability(models.Model):
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
        start = now() + timedelta(minutes=15)
        return self.filter(projection__date__lte=start)


class VolunteerSchedule(models.Model):
    projection = models.ForeignKey('Projection')
    volunteer_1 = models.ForeignKey('Volunteer', related_name='volunteer_1')
    volunteer_2 = models.ForeignKey('Volunteer', null=True, blank=True,
                                    related_name='volunteer_2')

    objects = ScheduleQuerySet.as_manager()

    def __str__(self):
        return "{}: {}, {}".format(self.projection,
                                   self.volunteer_1, self.volunteer_2)


class Laptop(models.Model):
    pass
