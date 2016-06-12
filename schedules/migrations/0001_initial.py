# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings
import dental_system.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dentists', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('is_active', models.BooleanField(db_index=True, default=False)),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('created_time', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('modified_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('date', models.DateTimeField()),
                ('anamnese', models.TextField()),
                ('created_by', models.ForeignKey(verbose_name='created by', to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(to='customers.Customer')),
                ('dentist', models.ForeignKey(to='dentists.Dentists')),
                ('modified_by', models.ForeignKey(verbose_name='modified by', related_name='+', null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DentistsSchedules',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('is_active', models.BooleanField(db_index=True, default=False)),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('created_time', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('modified_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('schedule_date', models.DateField(db_index=True)),
                ('time_start', models.TimeField(db_index=True)),
                ('time_end', models.TimeField(db_index=True)),
                ('created_by', models.ForeignKey(verbose_name='created by', to=settings.AUTH_USER_MODEL)),
                ('dentists', models.ForeignKey(to='dentists.Dentists')),
                ('modified_by', models.ForeignKey(verbose_name='modified by', related_name='+', null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleName',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('is_active', models.BooleanField(db_index=True, default=False)),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('created_time', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('modified_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('day', dental_system.fields.NameField(max_length=70, db_index=True)),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField()),
                ('created_by', models.ForeignKey(verbose_name='created by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(verbose_name='modified by', related_name='+', null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterIndexTogether(
            name='dentistsschedules',
            index_together=set([('schedule_date', 'time_start', 'time_end'), ('schedule_date', 'time_start')]),
        ),
    ]
