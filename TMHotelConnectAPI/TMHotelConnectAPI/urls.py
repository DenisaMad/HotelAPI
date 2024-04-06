"""
URL configuration for TMHotelConnectAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from UsersApp.Views.Taskviews import TaskViewWithoutPk , TaskViewWithPk
from UsersApp.Views.Userviews import UserViewWithoutPk, UserViewWithPk
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from UsersApp.Views.Roomviews import RoomViewWithoutPk , RoomViewWithPk, change_room_status

from UsersApp.Views.AssignRoom import AssignTasksToRoom,Unassigntask

from UsersApp.Views.RoomList  import RoomListByFloor
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView,
    TokenVerifyView
)
from UsersApp.Views.RoomList  import RoomListByFloor
from django.urls import path, include
from django import views




from UsersApp.Views.Userviews import MyTokenObtainPairView 

schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),

    
    path("api/task/<str:pk>/",TaskViewWithPk.as_view(),name="TASKWITHPK"),
    path("api/task/",TaskViewWithoutPk.as_view(),name="TASK"),


    path("api/user/<str:pk>/",UserViewWithPk.as_view(),name="USERWITHPK"),
    path("api/user/",UserViewWithoutPk.as_view(),name="USER"),
    path("api/room/",RoomViewWithoutPk.as_view(),name="ROOMWITHOUTPK"),
    path("api/unassign/<str:assign_id>/<str:task_id>/",Unassigntask,name="ROOMWITHOUTPK"),
    path("api/room/change_status/<str:id>/<str:status>/",change_room_status,name="ROOMWITHOUTPK"),
    path("api/room/<str:pk>/",RoomViewWithPk.as_view(),name = "ROOMWITHPK"),
    path("api/assign_room/",AssignTasksToRoom.as_view(),name="ASSIGNROOM"),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("api/login/",MyTokenObtainPairView.as_view(),name = "token_obtain_pair"),
    path("api/refresh/",TokenRefreshView.as_view(),name = "token_refresh"),  
     path('api/rooms/<str:floor>/', RoomListByFloor.as_view(), name='room_list_by_floor'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
