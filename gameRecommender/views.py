from django.shortcuts import render
from .models import GameInfo


def index(request):
    #game_list = GameInfo.objects.order_by('app_ID')[:]
    context = {'game_list': GameInfo.objects.all()}
    return render(request, 'gameRecommender/index.html', context)
