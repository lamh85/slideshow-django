from django.http import HttpResponse
import logging

def index(request):
    # print(request)
    # logging.info(request)
    logging.info("request")
    return HttpResponse("Hello, world.")
    # return HttpResponse(request)