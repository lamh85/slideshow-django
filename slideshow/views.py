from django.http import HttpResponse
import logging
import json

def index(request):
    request_body = request.body
    body_dict = json.loads(request_body.decode("utf-8"))

    logger = logging.getLogger("general")
    logger.info(body_dict["property"])

    return HttpResponse("Hello, world.")