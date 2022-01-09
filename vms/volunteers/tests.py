from django.utils.timezone import timedelta, now
from django.test import TestCase

from vms.entities.models import (
    Volunteer, VolunteerSchedule, Projection, Movie, Location)


class VolunteerScheduleModelTests(TestCase):
    def setUp(self):
        Location.objects.create(name='test location',
                                manager_name='test manager',
                                manager_phone='0123 456 789')
        Movie.objects.create(original_title='og title',
                             english_title='en title',
                             romanian_title='ro title',
                             duration=timedelta(minutes=15))
        Projection.objects.create(date=now(),
                                  location=Location.objects.first(),
                                  movie=Movie.objects.first())
        Projection.objects.create(date=now() + timedelta(days=2),
                                  location=Location.objects.first(),
                                  movie=Movie.objects.first())
        Volunteer.objects.create(name='test volunteer 1',
                                 email='test email',
                                 age=20,
                                 phone_1='0123 456 789')
        Volunteer.objects.create(name='test volunteer 2',
                                 email='test email',
                                 age=20,
                                 phone_1='0123 456 789')

    def test_volunteer_schedule(self):
        v1 = Volunteer.objects.get(name='test volunteer 1')
        v2 = Volunteer.objects.get(name='test volunteer 2')
        VolunteerSchedule.objects.create(projection=Projection.objects.first(),
                                         volunteer_1=v1)
        VolunteerSchedule.objects.create(projection=Projection.objects.last(),
                                         volunteer_1=v2,
                                         volunteer_2=v1)
        self.assertEquals(v1.schedule.count(), 2)
        self.assertEquals(v2.schedule.count(), 1)

    def test_current_schedule_shows_up_when_it_has_to(self):
        proj = Projection.objects.first()
        VolunteerSchedule.objects.create(projection=Projection.objects.first(),
                                         volunteer_1=Volunteer.objects.first())
        self.assertEquals(VolunteerSchedule.objects.current().count(), 1)

        # projection starts in more than 15 minutes
        proj._set_date(now() + timedelta(minutes=20))
        self.assertEquals(VolunteerSchedule.objects.current().count(), 0)

        # projection starts in 15 minutes
        proj._set_date(now() + timedelta(minutes=15))
        self.assertEquals(VolunteerSchedule.objects.current().count(), 1)

        # projection is ending now
        proj._set_date(now() - proj.movie.duration + timedelta(seconds=1))
        self.assertEquals(VolunteerSchedule.objects.current().count(), 1)

        # projection has ended
        proj._set_date(now() - proj.movie.duration - timedelta(minutes=1))
        self.assertEquals(VolunteerSchedule.objects.current().count(), 0)
