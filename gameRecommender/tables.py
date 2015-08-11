__author__ = 'Dean'

import django_tables2 as tables
from gameRecommender.models import GameInfo

class GameTable(tables.Table):
    class Meta:
        model = GameInfo
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}