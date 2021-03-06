# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 19:24
from __future__ import unicode_literals

import api.models.models_helper
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='/home/kostya/dev/blog/env/bin/easylearning/main_project/media/avatar/default.png', upload_to=api.models.user_profile.upload_avatar)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_profile',
            },
        ),
    ]
