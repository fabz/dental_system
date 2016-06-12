# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import dental_system.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Treatments',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('is_active', models.BooleanField(db_index=True, default=False)),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('created_time', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('name', dental_system.fields.NameField(db_index=True, max_length=70)),
                ('description', models.TextField()),
                ('treatment_type', models.SmallIntegerField(db_index=True, choices=[(0, 'Treatment'), (1, 'Preventive'), (2, 'Cosmetics'), (3, 'Heavy')], default=0)),
                ('created_by', models.ForeignKey(verbose_name='created by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(verbose_name='modified by', to=settings.AUTH_USER_MODEL, related_name='+', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
