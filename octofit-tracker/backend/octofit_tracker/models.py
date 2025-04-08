from mongoengine import Document, StringField, EmailField, ReferenceField, ListField, IntField

class User(Document):
    username = StringField(max_length=100, required=True)
    email = EmailField(unique=True, required=True)
    password = StringField(max_length=100, required=True)

class Team(Document):
    name = StringField(max_length=100, required=True)
    members = ListField(ReferenceField(User))

class Activity(Document):
    user = ReferenceField(User, required=True)
    activity_type = StringField(max_length=100, required=True)
    duration = StringField(max_length=50, required=True)  # Represent duration as a string
    activity_id = StringField(unique=True, required=True)  # Add unique activity_id field

class Leaderboard(Document):
    user = ReferenceField(User, required=True)
    score = IntField(required=True)
    leaderboard_id = StringField(unique=True, required=True)  # Add unique leaderboard_id field

class Workout(Document):
    name = StringField(max_length=100, required=True)
    description = StringField()
