# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import dental_system.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendors',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('is_active', models.BooleanField(default=False, db_index=True)),
                ('is_deleted', models.BooleanField(default=False, db_index=True)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('name', dental_system.fields.NameField(max_length=70)),
                ('created_by', models.ForeignKey(verbose_name='created by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(related_name='+', verbose_name='modified by', null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
