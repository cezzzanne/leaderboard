from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import CustomUser, Team, Leaderboard, UserScore
from .serializers import LeaderboardSerializer


@csrf_exempt
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse(data={'success': 'true', 'userID': user.id})
        else:
            return JsonResponse(data={'success': 'false'})
    return JsonResponse(data={'success': 'false'})


@csrf_exempt
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        try:
            username = request.data['username']
            email = request.data['email']
            user = User.objects.create(username=username, email=email)
            password = request.data['password']
            user.set_password(password)
            user.save()
            custom_user = CustomUser(user=user)
            custom_user.save()
            team_name = request.data['teamName']
            team = Team(name=team_name)
            team.save()
            team.players.add(custom_user)
            team.save()
            authenticate(username=username, password=password)
            return JsonResponse(data={'success': 'true', 'userID': user.id, 'teamID': team.id, 'username': username, 'teamName': team_name})
        except Exception as e:
            print(str(e))


@api_view(['POST'])
@csrf_exempt
def add_score(request):
    if request.method == 'POST':
        try:
            user_id = request.data['userID']
            leaderboard_id = request.data['leaderboardID']
            points = request.data['points']
            user = User.objects.get(id=user_id)
            custom_user = CustomUser.objects.get(user=user)
            leaderboard = Leaderboard.objects.get(id=leaderboard_id)
            user_score = UserScore(points=points, leaderboard=leaderboard, custom_user=custom_user)
            user_score.save()
            leaderboard_serialized = LeaderboardSerializer(leaderboard)
            return JsonResponse(data={'success': 'true', 'leaderboard': leaderboard_serialized.data})
        except Exception as e:
            print(str(e))



@csrf_exempt
@api_view(['GET'])
def get_leaderboard(request, lid):
    if request.method == 'GET':
        try:
            team = Team.objects.get(id=lid)
            leaderboard = Leaderboard.objects.filter(team=team)
            leaderboard_serialized = LeaderboardSerializer(leaderboard, many=True)
            return JsonResponse(data={'success': 'true', 'leaderboard': leaderboard_serialized.data})
        except Exception as e:
            print(str(e))


@csrf_exempt
@api_view(['POST'])
def add_leaderboard(request):
    if request.method == 'POST':
        try:
            team = Team.objects.get(id=request.data['teamID'])
            leaderboard = Leaderboard(team=team)
            leaderboard.save()
            leaderboard_s = Leaderboard.objects.filter(team=team)
            leaderboard_serialized = LeaderboardSerializer(leaderboard_s, many=True)
            return JsonResponse(data={'success': 'true', 'leaderboard': leaderboard_serialized.data})
        except Exception as e:
            print(str(e))
