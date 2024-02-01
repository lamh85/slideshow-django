from django.http import HttpResponse
import json
from . import location_service

def index(request):
    request_body = request.body
    params = json.loads(request_body.decode("utf-8"))

    location_result = location_service.get_location_name(params)

    return HttpResponse(location_result)