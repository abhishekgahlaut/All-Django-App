# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casino_finder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casino',
            name='created_by',
            field=models.ForeignKey(related_name='created_by', blank=True, to='casino_finder.User', null=True),
        ),
        migrations.AlterField(
            model_name='casino',
            name='modified_by',
            field=models.ForeignKey(related_name='modified_by', blank=True, to='casino_finder.User', null=True),
        ),
    ]
