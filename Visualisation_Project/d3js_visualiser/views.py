import json, re
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.db.models import Count, Min, Avg, Max, Q
from . import models
from decimal import Decimal

def home(request):
    filtering_options = {}
    for f in models.Person._meta.get_fields():
        if f.name == 'id' or f.name.startswith('PWGTP'):
            continue
        if f.choices:
            filtering_options[f.name] = {'verbose_name':f.verbose_name, 'choices':f.choices}
        else:
            filtering_options[f.name] = {'verbose_name':f.verbose_name}

    state_codes = {format(s.code, '02'): (s.abbreviation, s.name) for s in models.State.objects.filter(code__lte=72)} # other countries use codes greater than 72

    return render(request, 'd3js_visualiser/index.html', {'choices':json.dumps(filtering_options), 'state_codes':json.dumps(state_codes)})

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
        print val
        if isinstance(val, Decimal):
            data[format(pp.ST, '02')] = float(val)
        else:
            data[format(pp.ST, '02')] = val

    return HttpResponse(json.dumps(data), content_type = "application/json")

def choropleth_state(request):
    request_data =  get_to_dict(request.GET)
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

def chord(request):
    data = {}
    data['something'] = 'useful'
    return HttpResponse(json.dumps(data), content_type = "application/json")

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


def sunburst(request):
    data = {}
    data['something'] = 'useful'
    return HttpResponse(json.dumps(data), content_type = "application/json")

GET_DICT = re.compile('^([A-Za-z]+)\[([A-Za-z]+)\]$')
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
            raise Exception('Invalid key in the GET data: {}'.format(key))
    return rtn
