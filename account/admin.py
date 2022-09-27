from django.contrib import admin

# Register your models here.
import nested_admin
from django.db.models import Avg

from account.models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_filter = ['group']
    list_display = ['email', 'name', 'last_name', 'phone_number',
                    'group', 'place_rating', 'total_score']
    search_fields = ['name', 'second_name', 'phone_number']


class LeaderBoardProxy(CustomUser):
    class Meta:
        proxy = True
        verbose_name = 'Leaderboard'
        verbose_name_plural = 'Leaderboard'


@admin.register(LeaderBoardProxy)
class LeaderBoard(admin.ModelAdmin):
    list_display = ['email', 'name', 'last_name', 'group',
                    'phone_number', 'total_score', 'place_rating']
    list_filter = ['group']
    search_fields = ['name', 'second_name', 'phone_number']



