from django.contrib import admin
from . models import Contact 

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):    
    list_display = ('message',)
    list_filter = ('message',)
    search_fields = ('message',)