import os, sys, csv, threading, time
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Visualisation_Project.settings")
import django
django.setup()
from d3js_visualiser.models import Person, House, State, PublicUseMicrodataArea
from columns import housing_columns, person_columns, ST

def get_state_name(sc):
    for t in ST:
        if t[0] == sc:
            return t[1][:-3]

def get_state_abbreviation(sc):
    for t in ST:
        if t[0] == sc:
            return t[1][-3:]


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
            self.last_value = self.current_count

pu = ProgressUpdater(total_count=1343868) # housing counter

people = []
def hero():
    while True:
        try:
            people.pop().save()
        except IndexError:
            print 'my work here is done'
            time.sleep(1)

hero_thread = threading.Thread(target=hero)
hero_thread.daemon = True
hero_thread.start()

def create_person(row):
    p = Person()
    for col, val in enumerate(row):
        if col == 0:
            continue

        column_details = person_columns[col]

        if column_details[1] and len(val) == 0:
            continue
        elif not column_details[1] and len(val) == 0:
            print 'failed on col: {}, with value: '.format(col, val)
            print column_details
            print val
            print row
            raise Exception

        if col == 3 or col == 76 or col == 89: # migpuma = 76, puma = 3, powpuma= 89
            puma = get_or_create_PUMA(int(val), int(row[col + 1]))
            setattr(p, column_details[0], puma)
        elif column_details[2]:
            setattr(p, column_details[0], val)
        else:
            try:
                setattr(p, column_details[0], int(val))
            except ValueError as err:
                print 'column for error: {}'.format(col)
                raise
    people.append(p)

def get_or_create_state(state_code):
    try:
        return State.objects.get(code=state_code)
    except:
        state = State(code=state_code, name=get_state_name(state_code), abbreviation=get_state_abbreviation(state_code))
        people.append(state)
        while len(people):
            pass
        return state

def get_or_create_PUMA(puma_id, state_code):
    try:
        try:
            return PublicUseMicrodataArea.objects.get(code=puma_id, state__code=state_code)
        except:
            state = get_or_create_state(state_code)
            puma = PublicUseMicrodataArea(code=puma_id, state=state)
            people.append(puma)
            while len(people):
                pass
            return puma
    except django.db.utils.IntegrityError:
        print puma_id, state_code


data = []
try:
    with open('C:\Users\Benjamin Riddell\Documents\University\SWEN439\pums\csv_pus\ss06pusa.csv', 'r') as input:
        input.next()
        for row in input:
            data.append(row)
        # number_of_rows = sum(1 for row in input) - 1
except MemoryError:
    print 'failed because of memory error with {} rows'.format(len(data))
    exit()
number_of_rows = len(data)
print 'loaded {} rows form the data'.format(number_of_rows)

pu = ProgressUpdater(total_count=number_of_rows) # persons counter

def parse(start, end):
    with open('C:\Users\Benjamin Riddell\Documents\University\SWEN439\pums\csv_pus\pus.csv', 'r') as input:
        row = 0
        while row < start:
            row = row + 1

        while row < end:
            pu.update_progress()
            create_person(data[row].split(','))
            row = row + 1

parse(0, number_of_rows + 1)
# threads = []
# for i in range(0, number_of_rows / 10000 + 1):
#     threads.append(threading.Thread(target=parse, args = (i * 10000, (i + 1) * 10000)))
#     threads[-1].daemon = True
#     threads[-1].start()
#     print 'threads started: {}'.format(len(threads))
#     # if i == 1:
#     #     break
#     if len(threads) > 4:
#         threads[-4].join()
#
# for thread in threads:
#     thread.join()
hero_thread.join()
