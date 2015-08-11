__author__ = 'Dean'

import django_tables2 as tables
from gameRecommender.models import GameInfo


class GameTable(tables.Table):

    game_tags_column = tables.Column(empty_values=(), accessor='gameTags')

    def render_game_tags_column(self, record):

        data = []
        game_id = record.app_ID
        game = GameInfo.objects.get(app_ID=game_id)
        tags = game.gameTags.filter().values('tags')

        for item in tags:
            data.append(item['tags'])

        return data

    class Meta:
        model = GameInfo
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}
