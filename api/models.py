from django.db import models
from django.contrib.auth.models import User


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='custom_user')


class Team(models.Model):
    code = models.IntegerField(default=000)
    name = models.CharField(max_length=150)
    players = models.ManyToManyField(CustomUser)


class Leaderboard(models.Model):
    end_date = models.DateField()
    submit_deadline = models.DateField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboards')


class UserScore(models.Model):
    points = models.IntegerField()
    leaderboard = models.ForeignKey(Leaderboard, on_delete=models.CASCADE, related_name='user_scores')
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_scores')