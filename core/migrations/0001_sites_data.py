# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 16:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


def add_site_data(apps, schema_editor):
    Site = apps.get_model('sites', 'Site')
    new_domain = 'site.django-unleashed.dev'
    new_name = 'Startup Organizer'
    site_id = getattr(settings, 'SITE_ID', 1)
    if Site.objects.exists():
        #  Site object exist. get it by id
        current_site = Site.objects.get(pk=site_id)
        current_site.domain = new_domain
        current_site.name = new_name
        current_site.save()
    else:
        #  Site instance does not exist, we create it.
        current_site = Site(
            pk=site_id,
            domain=new_name,
            name=new_name
        )
        current_site.save()


def remove_site_data(apps, schema_editor):
    Site = apps.get_model('sites', 'Site')
    current_site = Site.objects.get(
        pk=getattr(settings, 'SITE_ID', 1)
    )
    current_site.domain = 'example.com'
    current_site.name = 'example.com'
    current_site.save()


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            add_site_data,
            remove_site_data,
        ),
    ]