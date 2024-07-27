from django import forms
from .views import teams_list_view
from .models import Score_board

class FirstStage(forms.ModelForm):
    class Mets:
        model = Score_board
        fields = ['team','points']





