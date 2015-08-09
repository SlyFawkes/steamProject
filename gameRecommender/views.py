from django.shortcuts import render
from django.template.context import RequestContext
from django.http import HttpResponse
from .models import GameInfo


def index(request):
    #game_list = GameInfo.objects.order_by('app_ID')[:]
    context = {'game_list': GameInfo.objects.all()}
    return render(request, 'gameRecommender/index.html', context)
