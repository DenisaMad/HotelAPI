from rest_framework import serializers
from .models import Task
from .models import Room
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
    def create(self, validated_data):
       

        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
class UserSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=["email", "username", "is_active"]
