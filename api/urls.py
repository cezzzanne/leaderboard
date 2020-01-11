from django.contrib import admin
from django.urls import path, include
from .views import login, register, get_leaderboard, add_score, add_leaderboard

urlpatterns = [
    path('login', login),
    path('register', register),
    path('leaderboard/<int:lid>', get_leaderboard),
    path('leaderboard/score', add_score),
    path('leaderboard/add', add_leaderboard)
]
