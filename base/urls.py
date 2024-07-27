
from django.urls import path
from . import views


urlpatterns = [
    path('players/', views.players_list, name='players_list'),
    path('team_list/', views.teams_list_view, name='team_list'),
    path('second_stage/',views.second_stage,name='second_stage'),
   

]