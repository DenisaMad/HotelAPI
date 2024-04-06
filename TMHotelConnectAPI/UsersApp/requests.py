from rest_framework import serializers
from .models import Room

class CreateTaskRequest(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()

class CreateRoomRequest(serializers.Serializer):
    name=serializers.CharField()
    floor=serializers.CharField()
    number=serializers.CharField()
    type=serializers.CharField()
    status = serializers.CharField()
class CreateUserRequest(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    password2 = serializers.CharField()
    email = serializers.CharField() 
    role = serializers.IntegerField()
class UpdateUserRequest(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField() 
    role = serializers.IntegerField()
    is_active= serializers.BooleanField()
    user_id= serializers.IntegerField()
class AssignRoomRequest(serializers.Serializer):
    tasks=serializers.ListField()
    user=serializers.CharField()
    descriere=serializers.CharField()
    room=serializers.CharField()