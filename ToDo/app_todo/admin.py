from django.contrib import admin
from .models import ToDoModel


class ToDoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user']
    readonly_fields = ['date_created']

admin.site.register(ToDoModel, ToDoAdmin)
