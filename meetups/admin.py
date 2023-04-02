from django.contrib import admin
from .models import *

# Register your models here.

class MeetupAdmin(admin.ModelAdmin):
    list_display=('title' ,'slug','location',)
    list_filter=('title','location','date',)
    prepopulated_fields={'slug':('title',)}


admin.site.register(Meetup,MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)