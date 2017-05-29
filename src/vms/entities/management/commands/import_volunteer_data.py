import csv
from datetime import datetime, date

from django.core.management.base import BaseCommand

from vms.entities.models import Volunteer


class Command(BaseCommand):
    help = """Populate the Volunteers table."""
    fields = [
        "alocare departament", "Reclamatii", "observatii", "Nume", "Prenume",
        "Sex", "Telefon", "Mail", "Oras origine", "Cartier CJ", "Data nastere",
        "Poza", "Education", "Work", "3 skills", "Limbi straine", "Limba 1",
        "Limba 2", "Limba 3", "Limba 4", "Limba 5", "pasiuni", "definitie volu",
        "social network", "de ce TIFF?", "Ai mai fost?", "In ce dept",
        "Voluntar altundeva", "Unde ce ai facut", "Ce dept vrei 1",
        "Ce dept vrei 2", "Ce dept vrei 3", "ordinea pref.", "motiveaza",
        "sapt inainte", "inainte si dupa?", "2 iunie", "3 iunie", "4 iunie",
        "5 iunie", "6 iunie", "7 iunie", "8 iunie", "9 iunie", "10 iunie",
        "11 iunie", "dupa fest", "ce vei castiga?", "viata-film", "sectiune",
        "carnet sofer", "bicicleta", "marime tricou", "contact urgenta",
        "telefon", "de unde stii de TIFF?", "Vrei sa ne mai spui ceva?"
    ]

    def _get_age(self, date_string):
        born = date_string.replace(".", "/").replace(" ", "/")
        born = born.replace("martie", "03").replace("octombrie", "10")
        try:
            born = datetime.strptime(born, "%d/%m/%Y")
        except ValueError:
            return 0
        today = date.today()
        return today.year - born.year - (
            (today.month, today.day) < (born.month, born.day)
        )

    def _get_phone(self, phone):
        nr = phone.replace(" ", "").lstrip("+").lstrip("4").lstrip("0")
        if len(nr) != 9:
            return "0000 000 000"
        return "0{} {} {}".format(nr[0:3], nr[3:6], nr[6:9])

    def handle(self, *args, **options):
        nr = 0
        with open("volunteers.csv") as f:
            reader = csv.DictReader(f, fieldnames=self.fields)
            next(reader)
            for row in reader:
                _, created = Volunteer.objects.get_or_create(
                    email=row['Mail'],
                    defaults={
                        'name': "{} {}".format(row['Nume'], row['Prenume']),
                        'age': self._get_age(row['Data nastere']),
                        'phone_1': self._get_phone(row['Telefon'])
                    }
                )
                if created:
                    nr += 1
        print("Finished importing volunteers. Created {}".format(nr))
