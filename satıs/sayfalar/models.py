from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name= 'iletişim'
        verbose_name_plural= 'iletişim'


class Order(models.Model):
    ad = models.CharField(max_length=100)
    soyad = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefon = models.CharField(max_length=100)
    sipariş_detay = models.TextField(blank=True)

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name= 'sipariş'
        verbose_name_plural= 'siparişler'

