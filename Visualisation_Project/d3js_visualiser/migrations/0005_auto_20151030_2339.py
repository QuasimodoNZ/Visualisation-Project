# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('d3js_visualiser', '0004_auto_20151030_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='precomputedproperties',
            name='ST',
            field=models.IntegerField(default=1, verbose_name=b'State Code', choices=[(1, b'Alabama/AL'), (2, b'Alaska/AK'), (4, b'Arizona/AZ'), (5, b'Arkansas/AR'), (6, b'California/CA'), (8, b'Colorado/CO'), (9, b'Connecticut/CT'), (10, b'Delaware/DE'), (11, b'District of Columbia/DC'), (12, b'Florida/FL'), (13, b'Georgia/GA'), (15, b'Hawaii/HI'), (16, b'Idaho/ID'), (17, b'Illinois/IL'), (18, b'Indiana/IN'), (19, b'Iowa/IA'), (20, b'Kansas/KS'), (21, b'Kentucky/KY'), (22, b'Louisiana/LA'), (23, b'Maine/ME'), (24, b'Maryland/MD'), (25, b'Massachusetts/MA'), (26, b'Michigan/MI'), (27, b'Minnesota/MN'), (28, b'Mississippi/MS'), (29, b'Missouri/MO'), (30, b'Montana/MT'), (31, b'Nebraska/NE'), (32, b'Nevada/NV'), (33, b'New Hampshire/NH'), (34, b'New Jersey/NJ'), (35, b'New Mexico/NM'), (36, b'New York/NY'), (37, b'North Carolina/NC'), (38, b'North Dakota/ND'), (39, b'Ohio/OH'), (40, b'Oklahoma/OK'), (41, b'Oregon/OR'), (42, b'Pennsylvania/PA'), (44, b'Rhode Island/RI'), (45, b'South Carolina/SC'), (46, b'South Dakota/SD'), (47, b'Tennessee/TN'), (48, b'Texas/TX'), (49, b'Utah/UT'), (50, b'Vermont/VT'), (51, b'Virginia/VA'), (53, b'Washington/WA'), (54, b'West Virginia/WV'), (55, b'Wisconsin/WI'), (56, b'Wyoming/WY'), (72, b'Puerto Rico/PR')]),
            preserve_default=False,
        ),
        migrations.AlterIndexTogether(
            name='precomputedproperties',
            index_together=set([('metric_name', 'ST')]),
        ),
    ]
