from django.http import HttpResponse,HttpResponseRedirect
import datetime
from django.shortcuts import render,redirect
import itertools 
from .forms import FirstStage
from .forms import ScoreBoardFormSet
from .models import Team



def current_date(request):
    now = datetime.datetime.now()
    html = "<html><body> it is now %s.</body></html>" % now
    return HttpResponse(html)


def players_list(request):
    from .models import Player  # Przeniesienie importu do wnętrza funkcji
    players = Player.objects.all()
    return render(request, 'players_list.html', {'players': players})


def teams_list_view(request):
    team_list = list(Team.objects.all())
    combinations = list(itertools.combinations(team_list, 2))

    if request.method == 'POST':
        form = FirstStage(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/second_stage/')
    else:
        formset = ScoreBoardFormSet(queryset=FirstStage)

    print("Formset forms:", formset.forms)
    return render(request,'teams_list.html',{'formset':formset,'combinations':combinations})


def second_stage(request):
    return render(request,'second_stage.html')







