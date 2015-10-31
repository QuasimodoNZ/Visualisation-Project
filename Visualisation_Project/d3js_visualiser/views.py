import json, re
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.db.models import Count, Min, Avg, Max
from . import models

def home(request):
    filtering_options = {}
    for f in models.Person._meta.get_fields():
        if f.name == 'id' or f.name.startswith('PWGTP'):
            continue
        if f.choices:
            filtering_options[f.name] = {'verbose_name':f.verbose_name, 'choices':f.choices}
        else:
            filtering_options[f.name] = {'verbose_name':f.verbose_name}

    return render(request, 'd3js_visualiser/index.html', {'choices':json.dumps(filtering_options)})

def choropleth(request):
#     print request.GET
#     print request.GET['query']
    request_data =  get_to_dict(request.GET)
    print request_data
    options = request_data.get('query', {})
    if 'state' in request_data:
        options['ST'] = request_data['state']
    print 'we got to number 1'
    selection = models.Person.objects.filter(**options)

    ########
    print '***** LOOK HERE FOR AGGREGATING STUFF *****'
    if 'metric' not in request_data:
        print 'no metric found'
        processing = selection.values('PUMA__code').annotate(COUNT=Count('id'))
    elif request_data['aggregation'] == 'MIN':
        processing = selection.values('PUMA__code').annotate(MIN=Min(request_data['metric'][0]))
    elif request_data['aggregation'] == 'AVG':
        processing = selection.values('PUMA__code').annotate(AVG=Avg(request_data['metric'][0]))
    elif request_data['aggregation'] == 'MAX':
        processing =  selection.values('PUMA__code').annotate(MAX=Max(request_data['metric'][0]))
    ########
    print 'we got to number 2'
    print processing
    # processing = {}
    # counter = 0
    # try:
    #     for item in selection.iterator():
    #         counter = counter + 1
    #         t = processing.get(item.PUMA.code, [0, 0])
    #         t[0] += getattr(item, request_data['metric'][0])
    #         t[1] += 1
    #         processing[item.PUMA.code] = t
    # except:
    #     print "Unexpected error:", sys.exc_info()[0]
    # finally:
    #     print 'got to the finally clause'
    # print 'we got to number 3'
    data = {}
    for d in processing:
        data[format(d['PUMA__code'], '05')] = d[request_data['aggregation']]
    print data
    print 'we got to number 3'



#     controller = {
#                 'visualisation': 'choropleth-state',
#                 'state': 11,
#                 'query': {
#                     'OCCP': 3060,
#                     'SEX': 1,
#                 },
#                 'metric': ["WAGP", "PINCP"],
#             }

    return HttpResponse(json.dumps(data), content_type = "application/json")

# state level, state id -> value
# puma level, puma id -> value
## what we got

def chord(request):
    data = {}
    data['something'] = 'useful'
    return HttpResponse(json.dumps(data), content_type = "application/json")

def bar(request):
    data = {}
    data['something'] = 'useful'
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
