from django.db import models
from django.contrib.auth.models import User


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='custom_user')

    def get_current_score(self):
        acc = 0
        for score in self.user_scores.all():
            acc += score.points
        return acc

    def __str__(self):
        return self.user.username


class Team(models.Model):
    name = models.CharField(max_length=150)
    players = models.ManyToManyField(CustomUser)

    def __str__(self):
        return self.name + ' ' + str(self.id)


class Leaderboard(models.Model):
    end_date = models.DateField(auto_now=True)
    submit_deadline = models.DateField(auto_now=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboards')

    def __str__(self):
        return self.team.name


class UserScore(models.Model):
    points = models.IntegerField()
    leaderboard = models.ForeignKey(Leaderboard, on_delete=models.CASCADE, related_name='user_scores')
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_scores')

    def __str__(self):
        return self.custom_user.user.username

