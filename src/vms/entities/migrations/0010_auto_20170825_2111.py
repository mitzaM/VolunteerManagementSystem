# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-25 18:11
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0009_auto_20170704_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='availability',
            name='cid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, help_text='Unique PBS identifier', verbose_name='Content ID'),
        ),
        migrations.AddField(
            model_name='location',
            name='cid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, help_text='Unique PBS identifier', verbose_name='Content ID'),
        ),
        migrations.AddField(
            model_name='movie',
            name='cid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, help_text='Unique PBS identifier', verbose_name='Content ID'),
        ),
        migrations.AddField(
            model_name='projection',
            name='cid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, help_text='Unique PBS identifier', verbose_name='Content ID'),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='cid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, help_text='Unique PBS identifier', verbose_name='Content ID'),
        ),
        migrations.AddField(
            model_name='volunteerschedule',
            name='cid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, help_text='Unique PBS identifier', verbose_name='Content ID'),
        ),
    ]
