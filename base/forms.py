from django import forms
from .models import Score_board
from django.forms import modelformset_factory

class FirstStage(forms.ModelForm):
    class Meta:
        model = Score_board
        fields = "__all__"

ScoreBoardFormSet = modelformset_factory(Score_board,form = FirstStage, extra = 3)


