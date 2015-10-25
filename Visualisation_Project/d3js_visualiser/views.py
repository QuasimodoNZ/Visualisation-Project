import json, re
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from . import models

def home(request):
# housing
#     filtering
#         TYPE
#         ACR
#         AGS
#         BDS
#         BLD
#         BUS
#         HFL
#         KIT
#         MRGT
#         MRGX
#         PLM
#         RMS
#         RNTM
#         TEL
#         TEN
#         VACS
#         VAL
#         VEH
#         YBL
#         FES
#         FPARC
#         HHL
#         HHT
#         HUGCL
#         HUPAC
#         HUPAOC
#         HUPARC
#         LNGI
#         MV
#
#     metric
#         CONP
#         ELEP
#         FS
#         FULP
#         GASP
#         INSP
#         MHP
#         MRGI
#         MRGP
#         RMS
#         SMP
#         WATP
#         FINCP
#         GRNTP
#         GRPIP
#         HINCP
# persons
#
#     query_options = {}
    query_options = {}
    for f in models.Person._meta.get_fields():
        if f.name == 'id' or f.name.startswith('PWGTP'):
            continue
        if f.choices:
            query_options[f.name] = {'verbose_name':f.verbose_name, 'choices':f.choices}
        else:
            query_options[f.name] = {'verbose_name':f.verbose_name}

    return render(request, 'd3js_visualiser/index.html', {'choices':json.dumps(query_options)})

def choropleth(request):
#     print request.GET
#     print request.GET['query']
    request_data =  get_to_dict(request.GET)
    options = request_data.get('query', {})
    if 'state' in request_data:
        options['ST'] = request_data['state']

    selection = models.Person.objects.filter(**options)

    processing = {}
    for item in selection.iterator():
        t = processing.get(item.PUMA.code, [0, 0])
        t[0] += getattr(item, request_data['metric'][0])
        t[1] += 1
        processing[item.PUMA.code] = t

    data = {}
    for key, value in processing.iteritems():
        data[format(key, '05')] = value[0] / value[1]


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
