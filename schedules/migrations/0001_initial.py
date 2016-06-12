# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import dental_system.fields
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dentists', '0001_initial'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(db_index=True, default=False)),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('created_time', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('date', models.DateTimeField()),
                ('anamnese', models.TextField()),
                ('created_by', models.ForeignKey(verbose_name='created by', to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(to='customers.Customer')),
                ('dentist', models.ForeignKey(to='dentists.Dentists')),
                ('modified_by', models.ForeignKey(null=True, related_name='+', verbose_name='modified by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DentistsSchedules',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(db_index=True, default=False)),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('created_time', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('schedule_date', models.DateField(db_index=True)),
                ('time_start', models.TimeField(db_index=True)),
                ('time_end', models.TimeField(db_index=True)),
                ('created_by', models.ForeignKey(verbose_name='created by', to=settings.AUTH_USER_MODEL)),
                ('dentists', models.ForeignKey(to='dentists.Dentists')),
                ('modified_by', models.ForeignKey(null=True, related_name='+', verbose_name='modified by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleName',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(db_index=True, default=False)),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('created_time', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('day', dental_system.fields.NameField(db_index=True, max_length=70)),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField()),
                ('created_by', models.ForeignKey(verbose_name='created by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(null=True, related_name='+', verbose_name='modified by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterIndexTogether(
            name='dentistsschedules',
            index_together=set([('schedule_date', 'time_start'), ('schedule_date', 'time_start', 'time_end')]),
        ),
    ]
