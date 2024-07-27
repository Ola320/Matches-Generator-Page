from django.contrib import admin
from .models import Player, Team_name,Team,Score_board
# # Register your models here.
admin.site.register(Player)
admin.site.register(Team_name)
admin.site.register(Team)
admin.site.register(Score_board)

