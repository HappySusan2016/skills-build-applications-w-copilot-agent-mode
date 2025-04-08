from django.http import JsonResponse
from django.views import View
from .models import User, Team, Activity, Leaderboard, Workout

class UserListView(View):
    def get(self, request):
        users = User.objects.all()
        data = [{"username": user.username, "email": user.email} for user in users]
        return JsonResponse(data, safe=False)

class TeamListView(View):
    def get(self, request):
        teams = Team.objects.all()
        data = [{"name": team.name, "members": [member.username for member in team.members]} for team in teams]
        return JsonResponse(data, safe=False)

class ActivityListView(View):
    def get(self, request):
        activities = Activity.objects.all()
        data = [{"user": activity.user.username, "type": activity.activity_type, "duration": activity.duration} for activity in activities]
        return JsonResponse(data, safe=False)

class LeaderboardListView(View):
    def get(self, request):
        leaderboard = Leaderboard.objects.all()
        data = [{"user": entry.user.username, "score": entry.score} for entry in leaderboard]
        return JsonResponse(data, safe=False)

class WorkoutListView(View):
    def get(self, request):
        workouts = Workout.objects.all()
        data = [{"name": workout.name, "description": workout.description} for workout in workouts]
        return JsonResponse(data, safe=False)
