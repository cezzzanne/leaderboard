from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import CustomUser, Team, Leaderboard, UserScore
from .serializers import LeaderboardSerializer, LeaderboardIDSerializer


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


@csrf_exempt
@api_view(['GET'])
def get_leaderboard(request, lid):
    if request.method == 'GET':
        try:
            team = Team.objects.get(id=lid)
            leaderboard = Leaderboard.objects.filter(team=team).first()
            leaderboard_serialized = LeaderboardSerializer(leaderboard)
            return JsonResponse(data={'success': 'true', 'leaderboard': leaderboard_serialized.data})
        except Exception as e:
            print(str(e))

@csrf_exempt
@api_view(['GET'])
def list_leaderboards(request, user_id):
    # import pdb; pdb.set_trace()
    # user_id = 5
    user = User.objects.get(id=user_id)
    custom_user = user.custom_user
    teams = Team.objects.filter(players__in=[custom_user])
    leaderboards = Leaderboard.objects.filter(team__in=teams)
    serialized_leaderboards = LeaderboardIDSerializer(leaderboards, many=True)
    return JsonResponse(data={'success': 'true', 'leaderboards': serialized_leaderboards.data})

