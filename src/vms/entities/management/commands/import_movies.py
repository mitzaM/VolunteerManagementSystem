import csv
from datetime import timedelta

from django.core.management.base import BaseCommand

from vms.entities.models import Movie


class Command(BaseCommand):
    help = """Populate the Movies table."""
    fields = [
        "Film(package) english title", "Film(package) original title",
        "Film(package) local title", "Venue > Name", "Start day", "Start time",
        "Runtime screening only(minutes)"
    ]

    def handle(self, *args, **options):
        nr = 0
        with open("files/eventival.csv") as f:
            reader = csv.DictReader(f, fieldnames=self.fields)
            next(reader)
            for row in reader:
                _, created = Movie.objects.get_or_create(
                    original_title=row['Film(package) original title'],
                    defaults={
                        'english_title': row['Film(package) english title'],
                        'romanian_title': row['Film(package) local title'],
                        'duration': timedelta(minutes=int(row['Runtime screening only(minutes)'])),
                    }
                )
                if created:
                    nr += 1
        print("Finished importing movies. Created {}".format(nr))
