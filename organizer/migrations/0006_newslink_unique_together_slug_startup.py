# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 15:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0005_newslink_slug'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='newslink',
            unique_together=set([('slug', 'startup')]),
        ),
    ]