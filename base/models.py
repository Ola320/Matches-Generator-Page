from typing import Any
from django.db import models
from .views import teams_list

class Player(models.Model):
    name = models.CharField(max_length=50,blank=True,null=True)
    surname = models.CharField(max_length=50,blank=True,null=True)
    age = models.IntegerField()
    number = models.BigIntegerField()
    def __str__(self):
        return self.name.strip()
    

class Team_name(models.Model):
    team_name = models.CharField(max_length=200,blank=True,null=True)
    def __str__(self):
        return self.team_name
    
class Team(models.Model):
    team_n = models.ForeignKey(Team_name,on_delete=models.CASCADE)
    team_player = models.ManyToManyField(Player,related_name='teams')
    
    def __str__(self):
        return self.team_n.team_name

class Team_list(models.Model)
    

