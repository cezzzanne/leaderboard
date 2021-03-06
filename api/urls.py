from django.contrib import admin
from django.urls import path, include
from .views import login, register, get_leaderboard, add_score, add_leaderboard, list_leaderboards

urlpatterns = [
    path('login', login),
    path('register', register),
    path('leaderboard/<int:lid>', get_leaderboard),
    path('leaderboard/add-score', add_score),
    path('leaderboard/add', add_leaderboard),
    path('leaderboard/user/<int:user_id>', list_leaderboards),
]
