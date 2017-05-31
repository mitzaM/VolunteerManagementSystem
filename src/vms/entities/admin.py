from django.contrib import admin

from vms.entities.models import (
    Location, Movie, Volunteer, Projection, Availability, VolunteerSchedule
)


class AvailabilityInline(admin.TabularInline):
    model = Availability
    extra = 1


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'manager_name', 'manager_phone',
                    'assistant_1_name', 'assistant_1_phone',
                    'assistant_2_name', 'assistant_2_phone',
                    'laptop_sn']


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['original_title', 'english_title', 'romanian_title',
                    'duration', 'format', 'over18', 'spoken_language_1',
                    'spoken_language_2', 'original_subtitle',
                    'electronic_sub_1_language', 'electronic_sub_2_format']


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'age', 'phone_1', 'language_1',
                    'language_2', 'language_3', 'language_4']
    inlines = [AvailabilityInline]


@admin.register(Projection)
class ProjectionAdmin(admin.ModelAdmin):
    list_display = ['date', 'location', 'movie', 'two_volunteers',
                    'special_notes']


@admin.register(VolunteerSchedule)
class VolunteerScheduleAdmin(admin.ModelAdmin):
    list_display = ['volunteer', 'projection']
