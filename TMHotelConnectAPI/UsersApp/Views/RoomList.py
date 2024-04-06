from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Room
from ..serializers import RoomSerializer
from enum import Enum 

class ERoomStatus(Enum):
    ocupata_de_zi_murdar=1,
    ocupata_de_zi_curat=2,
    ocupata_de_iesit=3,
    liber_murdar=4,
    liber_verificat=5,
    liber_curat=6,
    mentenanta_indisponibil=7
class RoomListByFloor(APIView):
    def get(self, request, floor):
        floor = request.data['floor']


        rooms = Room.objects.filter(floor=floor)
        ocupata_de_zi_murdar=rooms.filter(status=1)
        ocupata_de_zi_curat=rooms.filter(status=2)
        ocupata_de_iesit=rooms.filter(status=3)
        liber_murdar=rooms.filter(status=4)
        liber_verificat=rooms.filter(status=5)
        liber_curat=rooms.filter(status=6)
        mentenanta_indisponibil=rooms.filter(status=7)

        ocupata_de_zi_murdar=RoomSerializer( ocupata_de_zi_murdar, many= True).data
        ocupata_de_zi_curat=RoomSerializer( ocupata_de_zi_curat, many= True).data
        ocupata_de_iesit=RoomSerializer( ocupata_de_iesit, many= True).data
        liber_murdar=RoomSerializer( liber_murdar, many= True).data
        liber_verificat=RoomSerializer( liber_verificat, many= True).data
        liber_curat=RoomSerializer( liber_curat, many= True).data
        mentenanta_indisponibil=RoomSerializer( mentenanta_indisponibil, many= True).data

        response={
            "ocupata_de_zi_murdar" : ocupata_de_zi_murdar,
            "ocupata_de_zi_curat" : ocupata_de_zi_curat,
            "ocupata_de_iesit" : ocupata_de_iesit,
            "liber_murdar": liber_murdar,
            "liber_verificat": liber_verificat,
            "liber_curat": liber_curat,
            "mentenanta_indisponibil": mentenanta_indisponibil
        }
        return Response({"data" : response}, status= status.HTTP_200_OK)
