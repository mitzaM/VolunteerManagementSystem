import csv
import pytz
from datetime import datetime, timedelta

from django.conf import settings
from django.core.management.base import BaseCommand

from vms.entities.models import Movie, Location, Projection


class Command(BaseCommand):
    help = """Populate the Movies table."""
    fields = [
        "Film (package) english title", "Film (package) original title",
        "Film (package) local title", "Venue > Name", "Start day", "Start time",
        "Runtime screening itself (minutes)"
    ]
    locations = {
        'Florin Piersic': "Florin Piersic",
        'Victoria': "Cinema Victoria",
        'Dacia Mănăştur': "Cinema Dacia",
        'Sapientia': "Universitatea Sapienția",
        'Urania ': "Urania",
        # 'Cercul Militar': "Cercul Militar",
        'CCS': "CCS",
        'Cinema City 3': "Iulius Mall 3",
        'Cinema City 4': "Iulius Mall 4",
        'Unirii OA': "Piața Unirii",
        'Biserica Sfânta Treime': "Churches",
        'Institutul Francez': "Institutul Francez",
        'H33': "H33",
        'Someş OA': "Someș Open Air",
        'Mărăşti': "Cinema Mărăști",
        'Bonţida': "Banffy Castle",
        'Vlaha': "Vlaha",
        # 'Sat Dâncu': "Sat Dâncu",
    }

    def handle(self, *args, **options):
        nr = 0
        with open("files/2018/projections 2.csv") as f:
            reader = csv.DictReader(f, fieldnames=self.fields)
            next(reader)
            for row in reader:
                movie, _ = Movie.objects.get_or_create(
                    original_title=row['Film (package) original title'],
                    defaults={
                        'english_title': row['Film (package) english title'],
                        'romanian_title': row['Film (package) local title'],
                        'duration': timedelta(minutes=int(
                            row['Runtime screening itself (minutes)'])),
                    }
                )
                date = pytz.timezone(settings.TIME_ZONE).localize(
                    datetime.strptime("{} {}".format(row["Start day"], row["Start time"]),
                                      "%d.%m.%Y %H:%M"))
                location = Location.objects.get(name=self.locations.get(row["Venue > Name"]))
                _, created = Projection.objects.get_or_create(date=date, location=location,
                                                              movie=movie)
                if created:
                    nr += 1
        print("Finished importing projections. Created {}".format(nr))
