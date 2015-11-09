import os, sys
from collections import defaultdict
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Visualisation_Project.settings")
import django
django.setup()
from d3js_visualiser.models import Person, RelationshipPairs
from django.core.exceptions import ObjectDoesNotExist

class ProgressUpdater():
    def __init__(self, *args, **kwargs):
        self.total_count = kwargs['total_count']
        self.current_count = 0
        self.last_value = -1

    def update_progress(self, amount=1):
        self.current_count = self.current_count + amount
        progress = int(100.0 * self.current_count/self.total_count)
        if progress != self.last_value:
            sys.stdout.write("\r%d%% %d" % (progress, self.current_count))
            sys.stdout.flush()
            self.last_value = progress
print 'counting people with the fields'
num_of_migrations = Person.objects.filter(MIGPUMA__isnull=False).count()
num_of_pow = Person.objects.filter(POWPUMA__isnull=False).count()
pu = ProgressUpdater(total_count=num_of_migrations)
print 'found ' + str(num_of_migrations + num_of_pow) + ' people'

print 'starting to process '+ str(num_of_migrations) +' migrations'
d = defaultdict(int)
for p in Person.objects.filter(MIGPUMA__isnull=False).iterator():
    d[(p.PUMA_id, p.MIGPUMA_id,)] += 1
    pu.update_progress()
print '\nfinished populating the defaultdict for migration relationships, now creating ' + str(len(d)) + ' relationship instances'

pu = ProgressUpdater(total_count=len(d))
l = []
for key, val in d.iteritems():
    l.append(RelationshipPairs(metric_name='MIGPUMA', source_id=key[0], destination_id=key[1], amount=val))
    pu.update_progress()
print '\nfinished creating instances, now doing bulk create'
RelationshipPairs.objects.bulk_create(l)
print 'finished bulk create for migrations'

#####
print 'starting to process ' + str(num_of_pow) + ' place of work'
pu = ProgressUpdater(total_count=num_of_pow)
d = defaultdict(int)
for p in Person.objects.filter(POWPUMA__isnull=False).iterator():
    d[(p.PUMA_id, p.POWPUMA_id,)] += 1
    pu.update_progress()
print '\nfinished populating the defaultdict for place of work relationships, now creating ' + str(len(d)) + ' relationship instances'

pu = ProgressUpdater(total_count=len(d))
l = []
for key, val in d.iteritems():
    l.append(RelationshipPairs(metric_name='POWPUMA', source_id=key[0], destination_id=key[1], amount=val))
    pu.update_progress()
print '\nfinished creating instances, now doing bulk create'
RelationshipPairs.objects.bulk_create(l)
print 'finished bulk create'
