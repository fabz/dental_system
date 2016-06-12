# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone
import dental_system.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Treatments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('is_active', models.BooleanField(default=False, db_index=True)),
                ('is_deleted', models.BooleanField(default=False, db_index=True)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('modified_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', dental_system.fields.NameField(max_length=70, db_index=True)),
                ('description', models.TextField()),
                ('treatment_type', models.SmallIntegerField(default=0, db_index=True, choices=[(0, 'Treatment'), (1, 'Preventive'), (2, 'Cosmetics'), (3, 'Heavy')])),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('modified_by', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='modified by', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
