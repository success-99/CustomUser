from django.contrib import admin
from users.models import CustomUser
from users.models import Saved
from django.contrib.auth.models import Group
# Register your models here.


class CustomAdmin(admin.ModelAdmin):
    list_display = ['username','first_name']


admin.site.unregister(Group)

admin.site.register(CustomUser,CustomAdmin )
admin.site.register(Saved)
