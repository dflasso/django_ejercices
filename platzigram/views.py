from django.http import HttpResponse
from django.http import JsonResponse
from datetime import datetime
import json

def plain_text(request):
    now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Oh, hi! Current serer time is {now}')


def json1(request):
    numbers = map(lambda x : int(x),request.GET["numbers"].split(","))
    return JsonResponse({ "numbers" : sorted(numbers)},json_dumps_params={'indent': 4})


def json2(request):
    numbers = map(lambda x : int(x),request.GET["numbers"].split(","))
    data = { "numbers" : sorted(numbers)}
    return HttpResponse( json.dumps(data ) , content_type='application/json' )