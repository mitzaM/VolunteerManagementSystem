# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 11:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0002_auto_20170528_1314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(choices=[(2, '2 iunie'), (3, '3 iunie'), (4, '4 iunie'), (5, '5 iunie'), (6, '6 iunie'), (7, '7 iunie'), (8, '8 iunie'), (9, '9 iunie'), (10, '10 iunie'), (11, '11 iunie')])),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entities.Volunteer')),
            ],
            options={
                'verbose_name_plural': 'Availabilities',
            },
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entities.Projection')),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entities.Volunteer')),
            ],
        ),
    ]