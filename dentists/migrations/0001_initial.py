# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone

import dental_system.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dentists',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('is_active', models.BooleanField(db_index=True, default=False)),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('created_time', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('name', dental_system.fields.NameField(max_length=70)),
                ('phone_number', models.CharField(db_index=True, max_length=20, unique=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('address', models.TextField(null=True)),
                ('birth_place', models.CharField(max_length=100, null=True)),
                ('birth_date', models.DateField(null=True)),
                ('specialization', models.SmallIntegerField(db_index=True, default=0, choices=[
                 (0, 'GP'), (1, 'Perio'), (2, 'Bedah Mulut'), (3, 'Konservasi Gigi'), (4, 'Ortho'), (5, 'Prostho'), (6, 'Pedo')])),
                ('created_by', models.ForeignKey(verbose_name='created by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(verbose_name='modified by', null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
