import sqlite3
from multiprocessing import Pool, Process, Queue, freeze_support
import os, sys, csv, threading, time
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Visualisation_Project.settings")
import django
from django.db.utils import IntegrityError, OperationalError
from django.db import transaction
django.setup()
from d3js_visualiser.models import Person, House, State, PublicUseMicrodataArea
from columns import housing_columns, person_columns, ST

def get_state_name(sc):
    for t in ST:
        if t[0] == sc:
            if sc <= 72:
                return t[1][:-3]
            else:
                return t[1]

def get_state_abbreviation(sc):
    for t in ST:
        if t[0] == sc:
            if sc <= 72:
                return t[1][-2:]
            else:
                return t[1]

class ProgressUpdater():
    def __init__(self, *args, **kwargs):
        self.total_count = kwargs['total_count']
        self.current_count = 0
        self.last_value = -1

    def update_progress(self):
        self.current_count = self.current_count + 1
        progress = int(100.0 * self.current_count/self.total_count)
        if progress != self.last_value:
            sys.stdout.write("\r%d%% %d" % (progress, self.current_count))
            sys.stdout.flush()
            self.last_value = progress

def create_person(row):
    person = {}
    for col, val in enumerate(row):
        if col == 0 or col == 5 or col == 77 or col == 90:
            continue

        column_details = person_columns[col]

        if column_details[1] and len(val) == 0:
            continue # home[column_details[0]] = None
        elif not column_details[1] and len(val) == 0:
            print 'failed on col: {}, with value: '.format(col, val)
            print column_details
            print val
            print row
            raise Exception
        elif col == 3 or col == 76 or col == 89: # migpuma = 76, puma = 3, powpuma= 89
            puma = get_or_create_PUMA(int(val), int(row[col + 1]))
            person[column_details[0] + '_id'] = puma.id # setattr(h, column_details[0], puma)
        elif column_details[2]:
            person[column_details[0]] = val # setattr(h, column_details[0], val)
        else:
            try:
                person[column_details[0]] = int(val) # setattr(h, column_details[0], int(val))
            except ValueError as err:
                print 'column for error: {}'.format(col)
                raise

    cols = ''
    vals = ''
    for col, val in person.items():
        cols = cols + col + ', '
        if isinstance(val, basestring):
            vals = vals + '\'' + val + '\', '
        else:
            vals = vals + str(val) + ', '
    return 'INSERT INTO d3js_visualiser_person ({}) VALUES ({})'.format(cols[:-2], vals[:-2])

def get_or_create_state(state_code):
    try:
        return State.objects.get(code=state_code)
    except State.DoesNotExist:
        print 'creating state: {}'.format(state_code)
        state = State(code=state_code, name=get_state_name(state_code), abbreviation=get_state_abbreviation(state_code))
        state.save()
        return state

def get_or_create_PUMA(puma_id, state_code):
        state = get_or_create_state(state_code)
        try:
            return PublicUseMicrodataArea.objects.get(code=puma_id, state=state)
        except PublicUseMicrodataArea.DoesNotExist:
            print 'creating puma: {}, {}'.format(puma_id, state_code)
            state = get_or_create_state(state_code)
            puma = PublicUseMicrodataArea(code=puma_id, state=state)
            puma.save()
            return puma

def worker(chunk):
    people = []
    for row in chunk:
        person = create_person(row.split(','))
        people.append(person)
    print 'worker finished'
    return people

if __name__ == '__main__':
    CHUNK_SIZE = 10000
    freeze_support()
    chunks = []
    with open('D:\pums\csv_pus\pus.csv', 'r') as input:
        input.next()
        data = []
        for row in input:
            data.append(row)
            if len(data) == CHUNK_SIZE:
                chunks.append(data)
                data = []
        chunks.append(data)
    print 'loaded {} chunks from the data'.format(len(chunks))

    conn = sqlite3.connect('C:\Users\Benjamin Riddell\Documents\University\SWEN439\Visualisation-Project\Visualisation_Project\db.sqlite3')
    conn.isolation_level = None
    cur = conn.cursor()
    pool = Pool(processes=8)

    chunk_counter = 0
    for chunk in pool.imap_unordered(worker, chunks):
        chunk_counter = chunk_counter + 1
        print 'saving chunk: {}'.format(chunk_counter)

        cur.execute('BEGIN')
        for command in chunk:
            try:
                cur.execute(command)
            except sqlite3.IntegrityError, sqlite3.OperationalError:
                raise Exception('Command failed: ' + command)
        conn.commit()
