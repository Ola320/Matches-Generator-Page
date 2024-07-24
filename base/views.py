from django.http import HttpResponse
import datetime
from django.shortcuts import render
from .models import Player
from .models import Team
import itertools 


def current_date(request):
    now = datetime.datetime.now()
    html = "<html><body> it is now %s.</body></html>" % now
    return HttpResponse(html)

def home(request):
    return render(request,'home.html')

def players_list(request):
    players = Player.objects.all()
    return render(request, 'players_list.html', {'players': players})

def teams_list_view(request):
    team_list = list(Team.objects.all())
    combinations = list(itertools.combinations(team_list,2))
    return render (request,'teams_list.html',{'combinations': combinations})