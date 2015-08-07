from django.db import models


# Create your models here.
class GameTags(models.Model):
    tags = models.CharField(unique=True, max_length=255)


class GameFeatures (models.Model):
    features = models.CharField(unique=True, max_length=255)


class GameInfo(models.Model):
    game_name = models.CharField(max_length=255)
    app_ID = models.PositiveIntegerField(unique=True)
    metascore = models.PositiveIntegerField()
    positive_review_numbers = models.PositiveIntegerField()
    negative_review_numbers = models.PositiveIntegerField()
    picture = models.URLField()
    gameTags = models.ManyToManyField(GameTags)
    gameFeatures = models.ManyToManyField(GameFeatures)
