from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

@csrf_exempt
def index(request):
    if request.method == 'POST' \
       and request.META['CONTENT_TYPE'] == 'application/json':
        request_json = json.loads(request.body.decode('utf-8'))
        response = {}
        response['message'] = "It works fine."
        response['query'] = request_json['query']
        response['results'] = ['dummy1', 'dummy2', 'dummy3']
        return HttpResponse(json.dumps(response),
                            content_type='application/json')
    else:
        return HttpResponse("It works.")
