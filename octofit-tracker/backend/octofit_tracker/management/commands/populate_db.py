from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.delete()
        Team.objects.delete()
        Activity.objects.delete()
        Leaderboard.objects.delete()
        Workout.objects.delete()

        # Create users
        users = [
            User(username='thundergod', email='thundergod@mhigh.edu', password='password1').save(),
            User(username='metalgeek', email='metalgeek@mhigh.edu', password='password2').save(),
            User(username='zerocool', email='zerocool@mhigh.edu', password='password3').save(),
            User(username='crashoverride', email='crashoverride@mhigh.edu', password='password4').save(),
            User(username='sleeptoken', email='sleeptoken@mhigh.edu', password='password5').save(),
        ]

        # Create teams
        team1 = Team(name='Blue Team', members=[users[0], users[1]]).save()
        team2 = Team(name='Gold Team', members=[users[2], users[3], users[4]]).save()

        # Create activities
        activities = [
            Activity(user=users[0], activity_type='Cycling', duration='1 hour', activity_id='activity1').save(),
            Activity(user=users[1], activity_type='Crossfit', duration='2 hours', activity_id='activity2').save(),
            Activity(user=users[2], activity_type='Running', duration='1.5 hours', activity_id='activity3').save(),
            Activity(user=users[3], activity_type='Strength', duration='30 minutes', activity_id='activity4').save(),
            Activity(user=users[4], activity_type='Swimming', duration='1.25 hours', activity_id='activity5').save(),
        ]

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(user=users[0], score=100, leaderboard_id='leaderboard1').save(),
            Leaderboard(user=users[1], score=90, leaderboard_id='leaderboard2').save(),
            Leaderboard(user=users[2], score=95, leaderboard_id='leaderboard3').save(),
            Leaderboard(user=users[3], score=85, leaderboard_id='leaderboard4').save(),
            Leaderboard(user=users[4], score=80, leaderboard_id='leaderboard5').save(),
        ]

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event').save(),
            Workout(name='Crossfit', description='Training for a crossfit competition').save(),
            Workout(name='Running Training', description='Training for a marathon').save(),
            Workout(name='Strength Training', description='Training for strength').save(),
            Workout(name='Swimming Training', description='Training for a swimming competition').save(),
        ]

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
