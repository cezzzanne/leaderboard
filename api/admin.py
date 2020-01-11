from django.contrib import admin
from .models import Team, CustomUser, Leaderboard, UserScore
# Register your models here.
admin.site.register(Team)
admin.site.register(CustomUser)
admin.site.register(Leaderboard)
admin.site.register(UserScore)