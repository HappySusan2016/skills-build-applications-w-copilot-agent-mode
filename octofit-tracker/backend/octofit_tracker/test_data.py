# Test data for the OctoFit Tracker application

test_users = [
    {"username": "thundergod", "email": "thundergod@mhigh.edu", "password": "password1"},
    {"username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "password2"},
    {"username": "zerocool", "email": "zerocool@mhigh.edu", "password": "password3"},
    {"username": "crashoverride", "email": "crashoverride@mhigh.edu", "password": "password4"},
    {"username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "password5"},
]

test_teams = [
    {"name": "Blue Team", "members": ["thundergod", "metalgeek"]},
    {"name": "Gold Team", "members": ["zerocool", "crashoverride", "sleeptoken"]},
]

test_activities = [
    {"user": "thundergod", "activity_type": "Cycling", "duration": "1 hour"},
    {"user": "metalgeek", "activity_type": "Crossfit", "duration": "2 hours"},
    {"user": "zerocool", "activity_type": "Running", "duration": "1.5 hours"},
    {"user": "crashoverride", "activity_type": "Strength", "duration": "30 minutes"},
    {"user": "sleeptoken", "activity_type": "Swimming", "duration": "1.25 hours"},
]

test_leaderboard = [
    {"user": "thundergod", "score": 100},
    {"user": "metalgeek", "score": 90},
    {"user": "zerocool", "score": 95},
    {"user": "crashoverride", "score": 85},
    {"user": "sleeptoken", "score": 80},
]

test_workouts = [
    {"name": "Cycling Training", "description": "Training for a road cycling event"},
    {"name": "Crossfit", "description": "Training for a crossfit competition"},
    {"name": "Running Training", "description": "Training for a marathon"},
    {"name": "Strength Training", "description": "Training for strength"},
    {"name": "Swimming Training", "description": "Training for a swimming competition"},
]
