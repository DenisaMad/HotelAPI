from django.contrib import admin
from .models import Profile, Role , AssignRoomTask ,Task , Room , RoomType, Task 
# Register your models here.

admin.site.register(Profile)
admin.site.register(Role)
admin.site.register(Task)
admin.site.register(AssignRoomTask)
admin.site.register(Room)
admin.site.register(RoomType)


