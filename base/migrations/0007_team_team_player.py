# Generated by Django 5.0.7 on 2024-07-24 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_team_team_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_player',
            field=models.ManyToManyField(related_name='teams', to='base.player'),
        ),
    ]
