from django.http import JsonResponse
from django.views import View
from .models import User, Team, Activity, Leaderboard, Workout

# Replace the base URL with the Codespace URL and localhost
BASE_URL = "https://[REPLACE-THIS-WITH-YOUR-CODESPACE-NAME]-8000.app.github.dev"
LOCALHOST_URL = "http://localhost:8000"

class UserListView(View):
    def get(self, request):
        users = User.objects.all()
        data = [{"username": user.username, "email": user.email} for user in users]
        return JsonResponse({"base_url": BASE_URL, "localhost_url": LOCALHOST_URL, "data": data}, safe=False)

class TeamListView(View):
    def get(self, request):
        teams = Team.objects.all()
        data = [{"name": team.name, "members": [member.username for member in team.members]} for team in teams]
        return JsonResponse({"base_url": BASE_URL, "localhost_url": LOCALHOST_URL, "data": data}, safe=False)

class ActivityListView(View):
    def get(self, request):
        activities = Activity.objects.all()
        data = [{"user": activity.user.username, "type": activity.activity_type, "duration": activity.duration} for activity in activities]
        return JsonResponse({"base_url": BASE_URL, "localhost_url": LOCALHOST_URL, "data": data}, safe=False)

class LeaderboardListView(View):
    def get(self, request):
        leaderboard = Leaderboard.objects.all()
        data = [{"user": entry.user.username, "score": entry.score} for entry in leaderboard]
        return JsonResponse({"base_url": BASE_URL, "localhost_url": LOCALHOST_URL, "data": data}, safe=False)

class WorkoutListView(View):
    def get(self, request):
        workouts = Workout.objects.all()
        data = [{"name": workout.name, "description": workout.description} for workout in workouts]
        return JsonResponse({"base_url": BASE_URL, "localhost_url": LOCALHOST_URL, "data": data}, safe=False)
