from django.contrib import admin
from django.contrib.auth.models import Group
from core.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "age", "gender"]
    search_fields = ["first_name", "last_name"]
    list_filter = ["gender"]


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
