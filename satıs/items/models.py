from django.db import models
from django.db.models.base import Model


class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name= 'kategori'
        verbose_name_plural= 'kategoriler'

class Tag(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=50, verbose_name="Ürünün Adı")
    title = models.CharField(max_length=50, verbose_name="Ürünün Başlığı")
    category = models.ForeignKey(Category, null=True, on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    description = models.TextField(blank=True, verbose_name="Ürün Açıklaması")
    image = models.ImageField(upload_to="items/%Y/%m/%d/", default="items/default.png")
    üretim_yeri = models.CharField(max_length=100, blank=True)
    üretim_tarihi = models.CharField(max_length=100, blank=True)
    lezzeti = models.CharField(max_length=100, blank=True)
    indirimsiz_fiyat = models.CharField(max_length=100, blank=True)
    fiyat = models.CharField(max_length=100, blank=True)
    stok = models.BooleanField(default=False, verbose_name='stokta')
    
    class Meta:
        verbose_name= 'ürün'
        verbose_name_plural= 'ürünler'
    

