# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casino_finder', '0003_auto_20170714_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='casino',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
