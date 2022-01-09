# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 13:14
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='assistant_name',
            field=models.CharField(blank=True, max_length=127, null=True, verbose_name='Assistant name'),
        ),
        migrations.AddField(
            model_name='location',
            name='assistant_phone',
            field=models.CharField(blank=True, help_text="Format: '0XXX XXX XXX'", max_length=50, null=True, validators=[django.core.validators.RegexValidator(message="Telephone number must be entered in the format '0XXX XXX XXX'", regex='^0\\d{3}\\s\\d{3}\\s\\d{3}$')], verbose_name='Assistant phone'),
        ),
        migrations.AlterField(
            model_name='location',
            name='manager_name',
            field=models.CharField(max_length=127, verbose_name='Manager name'),
        ),
        migrations.AlterField(
            model_name='location',
            name='manager_phone',
            field=models.CharField(help_text="Format: '0XXX XXX XXX'", max_length=50, validators=[django.core.validators.RegexValidator(message="Telephone number must be entered in the format '0XXX XXX XXX'", regex='^0\\d{3}\\s\\d{3}\\s\\d{3}$')], verbose_name='Manager phone'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.PositiveIntegerField(blank=True, help_text='Movie duration in minutes.', null=True, verbose_name='Duration (minutes)'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='electronic_sub_1_format',
            field=models.CharField(blank=True, max_length=127, null=True, verbose_name='Electronic subtitle 1 format'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='electronic_sub_1_language',
            field=models.CharField(blank=True, max_length=127, null=True, verbose_name='Electronic subtitle 1 language'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='electronic_sub_2_format',
            field=models.CharField(blank=True, max_length=127, null=True, verbose_name='Electronic subtitle 2 format'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='electronic_sub_2_language',
            field=models.CharField(blank=True, max_length=127, null=True, verbose_name='Electronic subtitle 2 language'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='format',
            field=models.CharField(blank=True, choices=[('dcp', 'DCP'), ('35', '35mm'), ('digital', 'Digital')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='over18',
            field=models.BooleanField(default=False, help_text='Is the movie rated R?', verbose_name='Over 18'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='romanian_name',
            field=models.CharField(max_length=127),
        ),
        migrations.AlterField(
            model_name='projection',
            name='two_volunteers',
            field=models.BooleanField(default=False, help_text='Needs two volunteers?'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='phone_1',
            field=models.CharField(help_text="Format: '0XXX XXX XXX'", max_length=50, validators=[django.core.validators.RegexValidator(message="Telephone number must be entered in the format '0XXX XXX XXX'", regex='^0\\d{3}\\s\\d{3}\\s\\d{3}$')]),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='phone_2',
            field=models.CharField(blank=True, help_text="Format: '0XXX XXX XXX'", max_length=50, null=True, validators=[django.core.validators.RegexValidator(message="Telephone number must be entered in the format '0XXX XXX XXX'", regex='^0\\d{3}\\s\\d{3}\\s\\d{3}$')]),
        ),
    ]