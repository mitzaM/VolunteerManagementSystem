# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 11:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0007_auto_20170602_1108'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projection',
            options={'ordering': ['date']},
        ),
        migrations.RemoveField(
            model_name='volunteerschedule',
            name='volunteer',
        ),
        migrations.AddField(
            model_name='volunteerschedule',
            name='volunteer_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volunteer_1', to='entities.Volunteer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='volunteerschedule',
            name='volunteer_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='volunteer_2', to='entities.Volunteer'),
        ),
    ]
