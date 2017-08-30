# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-10 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Survey', '0003_office_values'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office',
            name='space',
            field=models.CharField(choices=[('ISSUE1', (('R1B1', 'R1B1'), ('R2B1', 'R2B1'), ('R3B1', 'R3B1'))), ('ISSUE2', (('R1B2', 'R1B2'), ('R2B2', 'R2B2'), ('R3B2', 'R3B2'))), ('ISSUE3', (('R1B3', 'R1B3'), ('R2B3', 'R2B3'), ('R3B3', 'R3B3')))], max_length=4),
        ),
    ]
