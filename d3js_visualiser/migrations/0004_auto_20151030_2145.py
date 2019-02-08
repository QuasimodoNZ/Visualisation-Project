# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('d3js_visualiser', '0003_auto_20150920_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrecomputedProperties',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('metric_name', models.CharField(unique=True, max_length=30)),
                ('min', models.IntegerField()),
                ('avg', models.DecimalField(max_digits=10, decimal_places=2)),
                ('max', models.IntegerField()),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='house',
            name='FACRP',
            field=models.IntegerField(null=True, verbose_name=b'Lot size allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='FAGSP',
            field=models.IntegerField(null=True, verbose_name=b'Sales of Agricultural Products allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='FBDSP',
            field=models.IntegerField(null=True, verbose_name=b'Number of bedrooms allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='FBLDP',
            field=models.IntegerField(null=True, verbose_name=b'Units in structure allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='FBUSP',
            field=models.IntegerField(null=True, verbose_name=b'Business or medical office on property allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='FCONP',
            field=models.IntegerField(null=True, verbose_name=b'Condominium fee allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='FELEP',
            field=models.IntegerField(null=True, verbose_name=b'Electricity (monthly cost) allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='FFSP',
            field=models.IntegerField(verbose_name=b'Food stamp amount (yearly amount) allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='FFULP',
            field=models.IntegerField(null=True, verbose_name=b'House heating fuel (yearly cost) allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='FGASP',
            field=models.IntegerField(null=True, verbose_name=b'Gas (monthly cost) allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='FHFLP',
            field=models.IntegerField(null=True, verbose_name=b'House heating fuel allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='FINSP',
            field=models.IntegerField(null=True, verbose_name=b'Fire, hazard, flood insurance allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='FKITP',
            field=models.IntegerField(null=True, verbose_name=b'Complete kitchen facilities allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='FMHP',
            field=models.IntegerField(null=True, verbose_name=b'Mobile home costs allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='FMRGIP',
            field=models.IntegerField(null=True, verbose_name=b'Payment include fire, hazard, flood insurance allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='FMRGP',
            field=models.IntegerField(null=True, verbose_name=b'Regular mortgage payment allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='FMRGTP',
            field=models.IntegerField(null=True, verbose_name=b'Payment include real estate taxes allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='FMRGXP',
            field=models.IntegerField(null=True, verbose_name=b'Mortgage status allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='FMVYP',
            field=models.IntegerField(null=True, verbose_name=b'When moved into this house or apartment allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='FPLMP',
            field=models.IntegerField(null=True, verbose_name=b'Complete plumbing facilities allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='FRMSP',
            field=models.IntegerField(null=True, verbose_name=b'Rooms allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='FRNTMP',
            field=models.IntegerField(null=True, verbose_name=b'Meals included in rent allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='FRNTP',
            field=models.IntegerField(null=True, verbose_name=b'Monthly rent allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='FSMP',
            field=models.IntegerField(null=True, verbose_name=b'Second mortgage payment allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='FSMXHP',
            field=models.IntegerField(null=True, verbose_name=b'Home equity loan status allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='FSMXSP',
            field=models.IntegerField(null=True, verbose_name=b'Second mortgage status allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='FTAXP',
            field=models.IntegerField(null=True, verbose_name=b'Taxes on property allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='FTELP',
            field=models.IntegerField(null=True, verbose_name=b'Telephones in house allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='FTENP',
            field=models.IntegerField(null=True, verbose_name=b'Tenure allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='FVACSP',
            field=models.IntegerField(null=True, verbose_name=b'Vacancy status allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='FVALP',
            field=models.IntegerField(null=True, verbose_name=b'Value allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='FVEHP',
            field=models.IntegerField(null=True, verbose_name=b'Vehicles available by household allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='FWATP',
            field=models.IntegerField(null=True, verbose_name=b'Water (yearly cost) allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='FYBLP',
            field=models.IntegerField(null=True, verbose_name=b'When structure first built allocation flag', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='house',
            name='WGTP80',
            field=models.IntegerField(verbose_name=b'Housing Weight replicate 80'),
        ),
    ]
