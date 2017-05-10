# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-22 20:10
from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0007_org_slug_nonunique'),
    ]

    operations = [
        migrations.AddField(
            model_name='remoterepository',
            name='project',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='remote_repository', to='projects.Project'),
        ),
    ]