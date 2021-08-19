from django.contrib import admin

# Register your models here.
from app1 import models
class NotesA(admin.ModelAdmin):
    list_display=["user","title","description"]
admin.site.register(models.Notes,NotesA)
admin.site.register(models.Homework)