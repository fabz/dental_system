# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings
import dental_system.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('is_active', models.BooleanField(db_index=True, default=False)),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('created_time', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('modified_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('customer_type', models.SmallIntegerField(db_index=True, choices=[(0, 'Patient'), (1, 'Prospect')], default=0)),
                ('name', dental_system.fields.NameField(db_index=True, max_length=70)),
                ('phone_number1', models.CharField(db_index=True, max_length=20)),
                ('phone_number2', models.CharField(db_index=True, null=True, max_length=20)),
                ('place_of_birth', models.CharField(null=True, max_length=100)),
                ('date_of_birth', models.DateField()),
                ('email', models.CharField(db_index=True, null=True, max_length=100)),
                ('address', models.TextField()),
                ('id_number', dental_system.fields.CodeField(db_index=True, max_length=40)),
                ('photo', models.TextField()),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('modified_by', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='modified by', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
