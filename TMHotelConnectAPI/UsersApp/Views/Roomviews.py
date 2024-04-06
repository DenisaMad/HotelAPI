from django.shortcuts import render
from rest_framework.decorators import APIView, api_view
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.password_validation import validate_password
from ..models import Room
from rest_framework.decorators import APIView
from rest_framework.response import Response
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from ..models import Room
from ..requests import CreateRoomRequest
from ..serializers import RoomSerializer
from drf_yasg.utils import swagger_auto_schema

class RoomViewWithoutPk(APIView):
    @swagger_auto_schema(request_body=CreateRoomRequest)
    def post(self,request):
        try:
            serializer = RoomSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Room created successfully"}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response({"error": "Floor and number should be integers"}, status=status.HTTP_400_BAD_REQUEST)
        except KeyError as e:
            missing_field = str(e).strip("'")
            return Response({"error": f"Field '{missing_field}' is required."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get(self, request):
        try:
            rooms = Room.objects.all()
            roomConverted = RoomSerializer(rooms, many=True)
            response = roomConverted.data
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            return Response("server exception",status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self,request):
        try:
            room = Room.objects.all()
            room.delete()
            return Response({"message":"Room deleted successfully"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response("server exception",status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class RoomViewWithPk(APIView):
         
        def get(self, request, pk):
            try:
                room = Room.objects.get(pk=pk)
                serializer = RoomSerializer(room)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Room.DoesNotExist:
                return Response("You room could not be found",status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response("server exception",status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        @swagger_auto_schema(request_body=CreateRoomRequest)
        def put(self, request, pk):
            try:
                room = Room.objects.get(pk=pk)
                serializer = RoomSerializer(room, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"message": "Room updated successfully"}, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Room.DoesNotExist:
                return Response({"error": "Room does not exist"}, status=status.HTTP_404_NOT_FOUND)
            except ValueError:
                return Response({"error": "Floor and number should be integers"}, status=status.HTTP_400_BAD_REQUEST)
            except KeyError as e:
                missing_field = str(e).strip("'")
                return Response({"error": f"Field '{missing_field}' is required."}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response("server exception try again later", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
        def delete(self,request, pk):
            try:
                room=Room.objects.get(pk=pk)
                room.delete()
                return Response({"message":"Room deleted successfully"}, status=status.HTTP_200_OK)
            except Room.DoesNotExist:
                return Response({"error":"Room does not exist"},status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@api_view(["PUT"])
def change_room_status(request, id, status):
    room=Room.objects.get(id=id)
    room.status=status
    room.save()
    return Response({"message":"Success"}, status=201)