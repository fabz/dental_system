# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import dental_system.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Treatments',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('is_active', models.BooleanField(db_index=True, default=True)),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('created_time', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('name', dental_system.fields.NameField(db_index=True, unique=True, max_length=70)),
                ('description', models.TextField()),
                ('treatment_type', models.SmallIntegerField(db_index=True, default=0, choices=[(0, 'Treatment'), (1, 'Preventive'), (2, 'Cosmetics'), (3, 'Heavy')])),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('modified_by', models.ForeignKey(related_name='+', null=True, to=settings.AUTH_USER_MODEL, verbose_name='modified by')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
