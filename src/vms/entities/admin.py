from django.contrib import admin

from vms.entities.models import Location, Movie, Volunteer, Projection


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'manager_name', 'manager_phone',
                    'assistant_name', 'assistant_phone']


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['original_name', 'romanian_name', 'duration', 'format',
                    'over18', 'spoken_language_1', 'spoken_language_2',
                    'original_subtitle', 'electronic_sub_1_language',
                    'electronic_sub_2_format']


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'age', 'phone_1', 'language_1',
                    'language_2', 'language_3', 'language_4']


@admin.register(Projection)
class ProjectionAdmin(admin.ModelAdmin):
    list_display = ['date', 'location', 'movie', 'two_volunteers',
                    'special_notes']
