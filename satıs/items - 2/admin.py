from django.contrib import admin
from django.db import models
from django.db.models.fields import SlugField
from items.models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    slug = models.SlugField()
   

class Foo(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField()