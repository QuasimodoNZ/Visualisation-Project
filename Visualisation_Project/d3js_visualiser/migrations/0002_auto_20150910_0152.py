# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('d3js_visualiser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='PUMA',
            field=models.ForeignKey(verbose_name=b'Public use microdata area code (PUMA) Designates area of 100,000 or more population. Use with ST for unique code. 00100..08200', to='d3js_visualiser.PublicUseMicrodataArea'),
        ),
    ]
