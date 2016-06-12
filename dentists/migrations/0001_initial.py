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
            name='Dentists',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(db_index=True, default=False)),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('created_time', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('modified_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', dental_system.fields.NameField(max_length=70)),
                ('phone_number', models.CharField(max_length=20, unique=True, db_index=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('address', models.TextField(null=True)),
                ('birth_place', models.CharField(max_length=100, null=True)),
                ('birth_date', models.DateField(null=True)),
                ('specialization', models.SmallIntegerField(choices=[(0, 'GP'), (1, 'Perio'), (2, 'Bedah Mulut'), (3, 'Konservasi Gigi'), (4, 'Ortho'), (5, 'Prostho'), (6, 'Pedo')], default=0, db_index=True)),
                ('created_by', models.ForeignKey(verbose_name='created by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(verbose_name='modified by', related_name='+', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
