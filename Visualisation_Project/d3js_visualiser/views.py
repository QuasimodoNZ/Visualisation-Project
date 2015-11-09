import json, re
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.db.models import Count, Min, Avg, Max, Q
from . import models, puma_groupings
from decimal import Decimal
from sets import Set
from collections import defaultdict

def home(request):
    filtering_options = {}
    for f in models.Person._meta.get_fields():
        if f.name == 'id' or f.name.startswith('PWGTP'):
            continue
        if f.choices:
            filtering_options[f.name] = {'verbose_name':f.verbose_name, 'choices':f.choices}
        else:
            filtering_options[f.name] = models.PrecomputedProperties.objects.filter(metric_name='Person_'+f.name).aggregate(min=Min('min'), max=Max('max'))
            filtering_options[f.name]['verbose_name'] = f.verbose_name

    state_codes = {format(s.code, '02'): (s.abbreviation, s.name) for s in models.State.objects.filter(code__lte=72)} # other countries use codes greater than 72

    return render(request, 'd3js_visualiser/index.html', {'choices':json.dumps(filtering_options), 'state_codes':json.dumps(state_codes), 'puma_to_group': puma_groupings.puma_to_group, 'group_to_puma': puma_groupings.group_to_puma})

#     controller = {
#                 'visualisation': 'choropleth-state',
#                 'state': 11,
#                 'query': {
#                     'OCCP': 3060,
#                     'SEX': 1,
#                 },
#                 'metric': ["WAGP", "PINCP"],
#             }

def choropleth_country(request):
    request_data =  get_to_dict(request.GET)
    print 'request data: ' + str(request_data)
    if 'metric' not in request_data:
        print 'handling request for population'
        metric_name = 'Person_POP'
        aggregation = 'COUNT'
    else:
        print 'handling request for ' + request_data['metric'][0]
        metric_name = 'Person_' + request_data['metric'][0]
        aggregation = request_data['aggregation']

    print 'metric_name: ' + metric_name
    print 'aggregation: ' + aggregation

    query = models.PrecomputedProperties.objects.filter(metric_name=metric_name)
    data = {}
    for pp in query:
        val = getattr(pp, aggregation.lower())
        if isinstance(val, Decimal):
            data[format(pp.ST, '02')] = float(val)
        else:
            data[format(pp.ST, '02')] = val

    return HttpResponse(json.dumps(data), content_type = "application/json")

def choropleth_state(request):
    request_data =  get_to_dict(request.GET)
    print 'request data: ' + str(request_data)
    options = request_data.get('query', {})
    options['ST'] = request_data['state']
    selection = models.Person.objects.filter(**options)

    if 'metric' not in request_data:
        processing = selection.values('PUMA__code').annotate(COUNT=Count('id'))
    elif request_data['aggregation'] == 'MIN':
        processing = selection.values('PUMA__code').annotate(MIN=Min(request_data['metric'][0]))
    elif request_data['aggregation'] == 'AVG':
        processing = selection.values('PUMA__code').annotate(AVG=Avg(request_data['metric'][0]))
    elif request_data['aggregation'] == 'MAX':
        processing =  selection.values('PUMA__code').annotate(MAX=Max(request_data['metric'][0]))

    # Gotta return the json data
    data = {}
    for d in processing:
        data[format(d['PUMA__code'], '05')] = d[request_data['aggregation']]

    return HttpResponse(json.dumps(data), content_type = "application/json")

def chord_country(request):

    data = []
    data['something'] = 'useful'
    return HttpResponse(json.dumps(data), content_type = "application/json")

def chord_state(request):
    request_data =  get_to_dict(request.GET)
    print 'request data: ' + str(request_data)
    options = request_data.get('query', {})
    options['ST'] = request_data['state']
    options['POWPUMA__state__code'] = request_data['state']
    # assumption is place of work, but we will get this from request_data eventually

    print 'options: ' + str(options)

    selection = models.Person.objects.filter(**options)
    counter = defaultdict(int)
    indicies = {}
    temp_groupings = {}
    for p in selection.values('PUMA__code', 'POWPUMA__code'):
        src = format(p['PUMA__code'], '05')
        dst = format(p['POWPUMA__code'], '05')
        if src in temp_groupings:
            src = temp_groupings[src]
        else:
            src = get_puma_group(options['ST'], src)
            temp_groupings[src] = src
        if dst in temp_groupings:
            dst = temp_groupings[dst]
        else:
            dst = get_puma_group(options['ST'], dst)
            temp_groupings[dst] = dst

        if src not in indicies:
            indicies[src] = len(indicies)
        if dst not in indicies:
            indicies[dst] = len(indicies)
        counter[(src, dst,)] += 1

    matrix = [[0] * len(indicies) for _ in xrange(len(indicies)) ]
    # matrix = [[0] * len(indicies)] * len(indicies)
    for key, val in counter.iteritems():
        row = indicies[key[0]]
        col = indicies[key[1]]
        matrix[row][col] = val

    # print 'indicies: ' + str(indicies)
    # print 'counter: ' + str(counter)
    # print 'matrix: ' + str(matrix)
    # data = []
    # data['something'] = 'useful'
    print 'number of rows and columns: ' + str(len(indicies))
    index_to_code = [None] * len(indicies)
    for code, index in indicies.iteritems():
        index_to_code[index] = code
    return HttpResponse(json.dumps({'matrix': matrix, 'indicies': index_to_code}), content_type = "application/json")

def bar_country(request):
    request_data =  get_to_dict(request.GET)

    if 'metric' not in request_data:
        # print 'handling request for population'
        metrics = ['POP']
        aggregation = 'COUNT'
    else:
        # print 'handling request for ' + request_data['metric'][0]
        metrics = request_data['metric']
        aggregation = request_data['aggregation']

    processing = {}
    for metric in metrics:
        query = models.PrecomputedProperties.objects.filter(metric_name='Person_'+metric)

        for pp in query:
            val = getattr(pp, aggregation.lower())
            if isinstance(val, Decimal):
                val = float(val)

            st = format(pp.ST, '02')
            datum = processing.get(st, {'id':st, 'metrics':[]})
            datum['metrics'].append([metric, val])
            processing[st] = datum

    data = []

    for key in processing:
        data.append(processing[key])

    return HttpResponse(json.dumps(data), content_type = "application/json")

def bar_state(request):
    request_data =  get_to_dict(request.GET)

    options = request_data.get('query', {})
    options['ST'] = request_data['state']
    selection = models.Person.objects.filter(**options)


    if 'metric' not in request_data:
        # print 'handling request for population'
        metrics = ['id']
        aggregation = 'COUNT'
    else:
        # print 'handling request for ' + request_data['metric'][0]
        metrics = request_data['metric']
        aggregation = request_data['aggregation']

    if aggregation == 'COUNT':
        class_ = Count
    elif aggregation == 'MIN':
        class_ = Min
    elif aggregation == 'AVG':
        class_ = Avg
    elif aggregation == 'MAX':
        class_ = Max

    processing = {}
    for metric in metrics:
        query = selection.values('PUMA__code').annotate(aggregation=class_(metric))
        # query = models.PrecomputedProperties.objects.filter(metric_name='Person_'+metric)
        print query
        for pp in query:
            val = pp['aggregation']
            if isinstance(val, Decimal):
                val = float(val)

            puma_id = format(pp['PUMA__code'], '05')
            datum = processing.get(puma_id, {'id':puma_id, 'metrics':[]})
            datum['metrics'].append([metric, val])
            processing[puma_id] = datum
            print 'got here: ' + puma_id
            print datum

    data = []

    for key in processing:
        data.append(processing[key])
    print data

    return HttpResponse(json.dumps(data), content_type = "application/json")


def force_country(request):
    data = {}
    data['something'] = 'useful'
    return HttpResponse(json.dumps(data), content_type = "application/json")

def force_state(request):
    request_data =  get_to_dict(request.GET)
    print 'request data: ' + str(request_data)
    options = request_data.get('query', {})
    options['ST'] = request_data['state']
    options['POWPUMA__state__code'] = request_data['state']
    # assumption is place of work, but we will get this from request_data eventually

    print 'options: ' + str(options)

    selection = models.Person.objects.filter(**options)
    print 'values: ' + str(selection.values('PUMA__code', 'POWPUMA__code'))

    counter = defaultdict(int)
    indicies = {}
    started = False
    for p in selection.values('PUMA__code', 'POWPUMA__code'):
        if not started:
            started = True
        src = format(p['PUMA__code'], '05')
        if src != get_puma_group(options['ST'], src):
            # print src + ' puma should be in group ' + get_puma_group(options['ST'], src)
            src = get_puma_group(options['ST'], src)

        dst = format(p['POWPUMA__code'], '05')
        if dst != get_puma_group(options['ST'], dst):
            # print 'dst was not pointing to group ' + dst + ': ' + get_puma_group(options['ST'], dst)
            # print src + ' puma should be in group ' + get_puma_group(options['ST'], src)
            dst = get_puma_group(options['ST'], dst)

        if src not in indicies:
            indicies[src] = len(indicies)
        if dst not in indicies:
            indicies[dst] = len(indicies)
        if src != dst:
            counter[(src, dst,)] += 1

    links = []
    nodes = [None] * len(indicies)

    for key, val in indicies.iteritems():
        nodes[val] = {'name': key, 'prestart_weight': 0}
    for key, val in counter.iteritems():
        link = {'source': indicies[key[0]], 'target': indicies[key[1]], 'value': val}
        nodes[link['source']]['prestart_weight'] += 1
        nodes[link['target']]['prestart_weight'] += 1
        links.append(link)
    # print 'data: ' + str(data)
    print 'indicies: ' + str(indicies)
    print 'links: ' + str(links)
    print 'nodes: ' + str(nodes)

    return HttpResponse(json.dumps({'links': links, 'nodes': nodes}), content_type = "application/json")

GET_DICT = re.compile('^([A-Za-z]+)\[([0-9A-Za-z_]+)\]$')
GET_LIST = re.compile('^([A-Za-z]+)\[\]$')
GET_VAR = re.compile('^([A-Za-z]+)$')

def get_to_dict(get_data):
    rtn = {}
    for key, value in get_data.iterlists():
        if key == '_':
            continue
        if GET_DICT.match(key):
            t = GET_DICT.match(key).groups()
            if t[0] not in rtn:
                rtn[str(t[0])] = {}
            rtn[str(t[0])][str(t[1])] = str(value[0]) #[str(v) for v in value]
        elif GET_LIST.match(key):
            rtn[str(GET_LIST.match(key).groups()[0])] = [str(v) for v in value]
        elif GET_VAR.match(key):
            rtn[str(GET_VAR.match(key).groups()[0])] = str(value[0])
        else:
            raise Exception('Invalid key in the GET data - key: {}, data: {}'.format(key, get_data))
    return rtn

def get_puma_group(state, puma):
    if state not in puma_groupings.groups:
        # print 'no groupings for ' + state
        return puma

    matchings = puma_groupings.groups[state]['matchings']
    for code, ranges in matchings.iteritems():
        if puma >= ranges[0] and puma <= ranges[1]:
            return code # is within the bounds for the group
    # print 'no mathcings found for {} in state {}: '.format(puma, puma_groupings.group[state]['name'], puma_groupings.group[state]['matchings'])
    # print 'no grouping for ' + state + ': '+ puma
    return puma # group found
