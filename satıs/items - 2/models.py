from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="media/%Y/%m/%d/")
    üretim_yeri = models.CharField(max_length=100, blank=True)
    üretim_tarihi = models.CharField(max_length=100, blank=True)
    lezzeti = models.CharField(max_length=100, blank=True)
    fiyat = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.name


