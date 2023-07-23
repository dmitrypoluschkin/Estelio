from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Cities
from .serializers import CitiesSerializer


# def index(request):
#   return HttpResponse("Hello, Bear", content_type="text/plain")


def index(request):
    qs = Cities.objects.all()
    data = CitiesSerializer(qs, many=True).data
    return JsonResponse(data, safe=False)
