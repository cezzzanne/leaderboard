from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Leaderboard, CustomUser, Team, UserScore


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class CustomUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    current_score = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = '__all__'

    def get_current_score(self, obj):
        return obj.get_current_score()


class TeamSerializer(serializers.ModelSerializer):
    players = CustomUserSerializer(read_only=True, many=True)

    class Meta:
        model = Team
        fields = '__all__'


class LeaderboardSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)

    class Meta:
        model = Leaderboard
        fields = '__all__'

class LeaderboardIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = ('id', 'name')
