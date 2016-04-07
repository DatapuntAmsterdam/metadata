# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-07 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atlas', '0003_initial_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='metadata',
            options={'ordering': ('-group', 'title')},
        ),
        migrations.AlterField(
            model_name='metadata',
            name='data_modified_date',
            field=models.CharField(blank=True, help_text='Versie datum gegevens (peildatum verwerkt product)', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='group',
            field=models.CharField(blank=True, help_text='Groep (optioneel)', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='last_import_date',
            field=models.DateField(blank=True, help_text='Laatst geimporteerd (wordt automatisch gevuld) / YYYY-MM-DD', null=True),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='title',
            field=models.CharField(blank=True, help_text='Titel', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='update_frequency',
            field=models.CharField(blank=True, help_text='Actualisatie (aanmaak producten)', max_length=100, null=True),
        ),
    ]
