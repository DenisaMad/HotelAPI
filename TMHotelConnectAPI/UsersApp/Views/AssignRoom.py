from rest_framework.decorators import APIView, api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import AssignRoomTask, Task, Room, User
from ..serializers import UserSerializer
from ..requests import AssignRoomRequest
from drf_yasg.utils import swagger_auto_schema


class AssignTasksToRoom(APIView):
    @swagger_auto_schema(request_body=AssignRoomRequest)
    def post(self, request):
        task_ids = request.data.get('tasks', [])  
        room_id = request.data.get('room')
        try:
            room = Room.objects.get(id=room_id)
            tasks = Task.objects.filter(id__in=task_ids)
            assign=AssignRoomTask()
            assign.descriere=request.data.get("descriere")
            assign.save()
            assign.tasks.set(tasks)
            assign.room=room
            assign.user_id=request.data.get("user")
            assign.save()
            return Response("Tasks assigned to room successfully", status=status.HTTP_201_CREATED)
        except Room.DoesNotExist:
            return Response("Room does not exist", status=status.HTTP_404_NOT_FOUND)
        except Task.DoesNotExist:
            return Response("One or more tasks do not exist", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)  
@api_view(["PUT"])
def Unassigntask(request, assign_id, task_id):
    assign= AssignRoomTask.objects.get(id=assign_id)
    task= Task.objects.get(id=task_id)
    assign.tasks.remove(task)
    assign.save()
    return Response("Task unassigned to room successfully", status=status.HTTP_201_CREATED)