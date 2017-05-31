import csv
from datetime import datetime

from django.core.management.base import BaseCommand
from django.utils.timezone import localtime

from vms.entities.models import Movie, Location, Projection


class Command(BaseCommand):
    help = """Populate the Movies table."""
    fields = [
        "Film(package) english title", "Film(package) original title",
        "Film(package) local title", "Venue > Name", "Start day", "Start time",
        "Runtime screening only(minutes)"
    ]
    locations = {
        'Urania ': "Urania",
        'Institutul Francez': "Institutul Francez",
        'Florin Piersic': "Florin Piersic",
        'Sapienţia': "Universitatea Sapienția",
        'Dacia Mănăştur': "Cinema Dacia",
        'Holy Trinity Church': "Holy Trinity Church",
        'Someş OA': "Someș Open Air",
        'Cinema City 4': "Iulius Mall 4",
        'Unirii OA': "Piața Unirii",
        'Sat Dâncu': "Sat Dâncu",
        'Cercul Militar': "Cercul Militar",
        'Cinema City 3': "Iulius Mall 3",
        'Mărăşti': "Cinema Mărăști",
        'Bonţida': "Banffy Castle",
        'Student House Cinema': "CCS",
        'Victoria': "Cinema Victoria",
        'Vlaha': "Vlaha"
    }

    def handle(self, *args, **options):
        nr = 0
        with open("eventival.csv") as f:
            reader = csv.DictReader(f, fieldnames=self.fields)
            next(reader)
            for row in reader:
                movie = Movie.objects.get(
                    original_title=row['Film(package) original title'])
                date = datetime.strptime("{} {}".format(
                    row["Start day"], row["Start time"]
                ), "%d.%m.%Y %H:%M")
                location = Location.objects.get(
                    name=self.locations.get(row["Venue > Name"]))

                _, created = Projection.objects.get_or_create(
                    date=localtime(date), location=location, movie=movie
                )
                if created:
                    nr += 1
        print("Finished importing projections. Created {}".format(nr))
