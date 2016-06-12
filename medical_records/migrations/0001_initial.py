# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
        ('dentists', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('treatments', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=False, db_index=True)),
                ('is_deleted', models.BooleanField(default=False, db_index=True)),
                ('created_time', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('date', models.DateTimeField()),
                ('anamnese', models.TextField()),
                ('diagnosis', models.TextField()),
                ('created_by', models.ForeignKey(verbose_name='created by', to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(to='customers.Customer')),
                ('dentist', models.ForeignKey(to='dentists.Dentists')),
                ('modified_by', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='modified by', null=True)),
                ('treatment', models.ForeignKey(to='treatments.Treatments')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
