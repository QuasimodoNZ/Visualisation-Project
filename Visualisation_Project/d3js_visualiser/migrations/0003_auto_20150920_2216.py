# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('d3js_visualiser', '0002_auto_20150910_0152'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='house',
            index_together=set([('ST', 'PUMA')]),
        ),
        migrations.AlterIndexTogether(
            name='person',
            index_together=set([('ST', 'PUMA')]),
        ),
    ]
