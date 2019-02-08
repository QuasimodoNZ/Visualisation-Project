# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('d3js_visualiser', '0007_auto_20151107_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelationshipPairs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('metric_name', models.CharField(max_length=30)),
                ('amount', models.IntegerField(verbose_name=b'Flow amount')),
                ('destination', models.ForeignKey(related_name='relationship_destination', to='d3js_visualiser.PublicUseMicrodataArea')),
                ('source', models.ForeignKey(related_name='relationship_source', to='d3js_visualiser.PublicUseMicrodataArea')),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='NAICSI',
            field=models.IntegerField(null=True, verbose_name=b'North American Industry Classification (NAICS) Categories', choices=[(1, b'Agriculture, Forestry, Fishing and Hunting'), (2, b'Mining'), (3, b'Utilities'), (4, b'Construction'), (5, b'Manufacturing'), (6, b'Wholesale Trade'), (7, b'Retail Trade'), (8, b'Transportation and Warehousing'), (9, b'Information'), (10, b'Finance and Insurance'), (11, b'Real Estate Rental and Leasing'), (12, b'Professional, Scientific, and Technical Services'), (13, b'Management of Companies and Enterprises'), (14, b'Administrative and Support and Waste Management and Remediation Services'), (15, b'Educational Services'), (16, b'Health Care and Social Assistance'), (17, b'Arts, Entertainment, and Recreation'), (18, b'Accommodation and Food Services'), (19, b'Other Services (except Public Administration)'), (20, b'Public Administration'), (21, b'Unemployed, with No Work Experience in the Last 5 Years')]),
        ),
        migrations.AlterField(
            model_name='person',
            name='SOCI',
            field=models.IntegerField(null=True, verbose_name=b'Standard Occupational Classifcation (SOC) Categories', choices=[(1, b'Management Occupations'), (2, b'Business and Financial Operations Occupations'), (3, b'Computer and Mathematical Occupations'), (4, b'Architecture and Engineering Occupations'), (5, b'Life, Physical and Social Sciene Occupations'), (6, b'Community and social service Occupations'), (7, b'Legal Occupations'), (8, b'Education, Training, and Library Occupations'), (9, b'Arts, Design, Entertainment, Sports, and Media Occupations'), (10, b'Healthcare Practitioners and Technical Occupations'), (11, b'Healthcare Support Occupations'), (12, b'Protective Service Occupations'), (13, b'Food Preparation and Serving Related Occupations'), (14, b'Building and Grounds Cleaning and maintenance Occupations'), (15, b'Personal Care and Service Occupations'), (16, b'Sales and Related Occupations'), (17, b'Office and Administrative Support Occupations'), (18, b'Farming, Fishing, and Forestry Occupations'), (19, b'Construction and Extraction Occupations'), (20, b'Installation, Maintenance, and Repair Occupations'), (21, b'Production Occupations'), (22, b'Transportation and Material Moving Occupations'), (23, b'Military Specific Occupations'), (24, b'Unemployed, With No Work Experience in the Last 5 Years')]),
        ),
        migrations.AlterUniqueTogether(
            name='relationshippairs',
            unique_together=set([('metric_name', 'source', 'destination')]),
        ),
        migrations.AlterIndexTogether(
            name='relationshippairs',
            index_together=set([('metric_name', 'source')]),
        ),
    ]
