
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('date/',views.current_date,name='current_date'),
    path('players/', views.players_list, name='players_list'),
    path('team_list/', views.teams_list_view, name='team_list'),

]