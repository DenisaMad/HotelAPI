from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Role(models.Model):
    grade = models.PositiveSmallIntegerField(blank=False,null=False)
    name = models.CharField(max_length=100,null=False,blank=False)
    def __str__(self):
        return self.name

class Profile(models.Model):
    profile_image = models.ImageField(blank=True,null=True,upload_to="images",default="images/placeholder.png")    
    email = models.EmailField(blank=False,null=False,unique=True)
    role = models.PositiveIntegerField(blank=True,null=True)
    user = models.OneToOneField(User, blank=False,null=False,on_delete=models.CASCADE)
    def __str__(self):
        return self.email
    
class Task(models.Model):
    name = models.CharField(blank=False,null=False,max_length=50)
    description = models.TextField(blank=False,null=False,default="No description")
    def __str__(self):
        return self.name
    
class RoomType(models.Model):
    name = models.CharField(max_length=100,blank=False,null=False)
    description = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=100,blank=False,null=False)
    floor = models.PositiveSmallIntegerField(blank=False,null=False,default=0)
    number = models.PositiveSmallIntegerField(blank=False,null=False,default=0)
    type = models.ForeignKey(RoomType,blank=True,null=True,on_delete=models.CASCADE)
    
    status = models.PositiveSmallIntegerField(max_length=100,blank=False,null=False,default=1)
    def __str__(self):
        return self.name

    
class AssignRoomTask(models.Model):
    tasks = models.ManyToManyField(Task, blank=True)#OBSERVATII SI AM ZIS DE 5 ORI
    user = models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)
    descriere = models.TextField(blank=True,null=True,default="")
    room = models.ForeignKey(Room,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.descriere
    
