from django.contrib import admin
from casino_finder.models import Casino
from casino_finder.user_models import User


class CasinoAdmin(admin.ModelAdmin):
    list_display = ('id','name','address')


admin.site.register(Casino)
admin.site.register(User)