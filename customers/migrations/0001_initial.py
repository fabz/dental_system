# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import dental_system.fields
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(db_index=True, default=False)),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('created_time', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('customer_type', models.SmallIntegerField(choices=[(0, 'Patient'), (1, 'Prospect')], db_index=True, default=0)),
                ('name', dental_system.fields.NameField(max_length=70, db_index=True)),
                ('phone_number1', models.CharField(max_length=20, db_index=True)),
                ('phone_number2', models.CharField(max_length=20, null=True, db_index=True)),
                ('place_of_birth', models.CharField(max_length=100, null=True)),
                ('date_of_birth', models.DateField()),
                ('email', models.CharField(max_length=100, null=True, db_index=True)),
                ('address', models.TextField()),
                ('id_number', dental_system.fields.CodeField(max_length=40, db_index=True)),
                ('photo', models.TextField()),
                ('created_by', models.ForeignKey(verbose_name='created by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(related_name='+', null=True, verbose_name='modified by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
