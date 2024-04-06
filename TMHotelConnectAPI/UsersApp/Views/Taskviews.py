from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.password_validation import validate_password
from ..models import Task
from rest_framework.decorators import APIView
from rest_framework.response import Response
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from ..models import User
#EXAMPLE OF CRUD OPERATIONS FOR CREATING A TASK:
from ..requests import CreateTaskRequest
from ..serializers import TaskSerializer
class TaskViewWithoutPk(APIView):

    @swagger_auto_schema(request_body=CreateTaskRequest)
    def post(self,request):
        data = request.data 
        response = TaskSerializer(data=data)
        if response.is_valid():
            response.save()
        else:
            return Response(response.errors,status=status.HTTP_201_CREATED)
        return Response("Success",status=status.HTTP_201_CREATED)
    def get(self,request):
        tasks = Task.objects.all()
        tasksConverted = TaskSerializer(tasks,many=True)
        response = tasksConverted.data
        return Response(response,status=status.HTTP_200_OK)



class TaskViewWithPk(APIView):
    def get(self,request,pk):
        task = Task.objects.get(id=pk)
        taskConverted = TaskSerializer(task,many=False)
        response = taskConverted.data
        return Response(response,status=status.HTTP_200_OK)
