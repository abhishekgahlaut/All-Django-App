# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casino_finder', '0002_auto_20170712_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casino',
            name='created_by',
            field=models.ForeignKey(related_name='casino_finder_casino_created_by', blank=True, to='casino_finder.User', null=True),
        ),
        migrations.AlterField(
            model_name='casino',
            name='modified_by',
            field=models.ForeignKey(related_name='casino_finder_casino_modified_by', blank=True, to='casino_finder.User', null=True),
        ),
    ]
