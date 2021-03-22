from django.db import models

# Create your models here.

class TeamList(models):
    team_name = models.CharField(max_length=200)
    games_played = models.IntegerField('games played')
    wins = models.IntegerField('wins')
    losses = models.IntegerField('losses')
    otl = models.IntegerField('otllosses')
    win_percentage = models.DecimalField(max_digits=7, decimal_places=4)
    loss_percentage = models.DecimalField(max_digits=7, decimal_places=4)

class GameLog(models):
    team_name = 