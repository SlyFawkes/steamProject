from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Josh is wrong, Dan is right, all hail Dan, also Python > Java")
