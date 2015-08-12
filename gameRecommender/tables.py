__author__ = 'Dean'

import django_tables2 as tables
from gameRecommender.models import GameInfo


class GameTable(tables.Table):

    game_tags_column = tables.Column(empty_values=(), accessor='gameTags')
    game_features_column = tables.Column(empty_values=(), accessor='gameFeatures')

    def render_game_tags_column(self, record):

        data = ''
        game_id = record.app_ID
        game = GameInfo.objects.get(app_ID=game_id)
        tags = game.gameTags.filter().values('tags')

        for item in tags:
            data += item['tags'] + ' '

        return data

    def render_game_features_column(self, record):

        data = ''
        game_id = record.app_ID
        game = GameInfo.objects.get(app_ID=game_id)
        features = game.gameFeatures.filter().values('features')

        for item in features:
            data += item['features'] + ' '

        return data

    class Meta:
        model = GameInfo
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}
