import os, sys
from multiprocessing import Pool, freeze_support
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Visualisation_Project.settings")
import django
from d3js_visualiser.models import Person
from django.db import transaction

from d3js_visualiser import choices

occupations = {
    'MGR': 1,
    'BUS': 2,
    'FIN': 3,
    'CMM': 4,
    'ENG': 5,
    'SCI': 6,
    'CMS': 7,
    'LGL': 8,
    'EDU': 9,
    'ENT': 10,
    'MED': 11,
    'HLS': 12,
    'PRT': 13,
    'EAT': 14,
    'CLN': 15,
    'PRS': 16,
    'SAL': 17,
    'OFF': 18,
    'FFF': 19,
    'CON': 20,
    'EXT': 21,
    'RPR': 22,
    'PRD': 23,
    'TRN': 24,
    'MIL': 25,
    'UNE': 26,
}
naicsi = {
    '11': 1,
    '21': 2,
    '22': 3,
    '23': 4,
    '31': 5,
    '32': 5,
    '33': 5,
    '3M': 5,
    '42': 6,
    '44': 7,
    '45': 7,
    '4M': 7,
    '48': 8,
    '49': 8,
    '51': 9,
    '52': 10,
    '53': 11,
    '54': 12,
    '55': 13,
    '56': 14,
    '61': 15,
    '62': 16,
    '71': 17,
    '72': 18,
    '81': 19,
    '92': 20,
    '99': 21,
}

soci = {
    '11': 1,
    '13': 2,
    '15': 3,
    '17': 4,
    '19': 5,
    '21': 6,
    '23': 7,
    '25': 8,
    '27': 9,
    '29': 10,
    '31': 11,
    '33': 12,
    '35': 13,
    '37': 14,
    '39': 15,
    '41': 16,
    '43': 17,
    '45': 18,
    '47': 19,
    '49': 20,
    '51': 21,
    '53': 22,
    '55': 23,
    '99': 24
}

def matchIDs(prefix, c, i):
    values = []
    for t in c:
        if t[i].startswith(prefix):
            values.append(t[0])
    return values



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

pu = ProgressUpdater(total_count=len(soci)+len(naicsi)+len(occupations))

for key, val in occupations.iteritems():
    values = matchIDs(key, choices.OCCP, 1)
    Person.objects.filter(OCCP__in=values).update(OCCI=val)
    pu.update_progress()
print '\nfinished OCCP'
for key, val in naicsi.iteritems():
    values = matchIDs(key, choices.NAICSP, 0)
    Person.objects.filter(NAICSP__in=values).update(NAICSI=val)
    pu.update_progress()
print '\nfinished NAICSP'
for key, val in soci.iteritems():
    values = matchIDs(key, choices.SOCP, 0)
    Person.objects.filter(SOCP__in=values).update(SOCI=val)
    pu.update_progress()
print '\nfinished SOCP and all fields'
