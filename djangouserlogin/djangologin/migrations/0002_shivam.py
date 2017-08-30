# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangologin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shivam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
