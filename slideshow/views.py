from django.http import HttpResponse
import logging
import json
from . import location_service

def index(request):
    request_body = request.body
    body_dict = json.loads(request_body.decode("utf-8"))

    logger = logging.getLogger("general")
    logger.info(body_dict["property"])

    location_result = location_service.get_location_name()

    return HttpResponse(location_result)