# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('d3js_visualiser', '0005_auto_20151030_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='precomputedproperties',
            name='avg',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='precomputedproperties',
            name='count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='precomputedproperties',
            name='max',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='precomputedproperties',
            name='metric_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='precomputedproperties',
            name='min',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='precomputedproperties',
            unique_together=set([('metric_name', 'ST')]),
        ),
        migrations.AlterIndexTogether(
            name='precomputedproperties',
            index_together=set([]),
        ),
    ]
