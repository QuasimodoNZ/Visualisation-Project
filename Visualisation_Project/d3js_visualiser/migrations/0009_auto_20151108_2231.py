# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('d3js_visualiser', '0008_auto_20151108_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationshippairs',
            name='amount',
            field=models.IntegerField(default=0, verbose_name=b'Flow amount'),
        ),
    ]
