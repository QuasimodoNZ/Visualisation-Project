import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Visualisation_Project.settings")
import django
django.setup()
from d3js_visualiser.models import Person, House, State, PublicUseMicrodataArea, PrecomputedProperties
from columns import housing_columns, person_columns, ST
from django.db.models import Min, Avg, Max, Count

# For the people records
fields = [f.name for f in Person._meta.get_fields() if not f.choices]
for f in fields[:]:
    if f.startswith('PWGTP') or f == 'id':
        fields.remove(f)

for field in fields:
    metric_name = 'Person_' + field
    results = Person.objects.values('ST').annotate(min=Min(field), avg=Avg(field), max=Max(field), count=Count(field))
    for result in results:
        PrecomputedProperties(metric_name=metric_name, min=result['min'], avg=result['avg'], max=result['max'], count=result['count'], ST=result['ST']).save()
    print 'completed Person.' + field

# For the housing records
fields = [f.name for f in House._meta.get_fields() if not f.choices]
for f in fields[:]:
    if f.startswith('WGTP') or f == 'id':
        fields.remove(f)

for field in fields:
    metric_name = 'House_' + field
    results = House.objects.values('ST').annotate(min=Min(field), avg=Avg(field), max=Max(field), count=Count(field))
    for result in results:
        PrecomputedProperties(metric_name=metric_name, min=result['min'], avg=result['avg'], max=result['max'], count=result['count'], ST=result['ST']).save()
    print 'completed House.' + field
