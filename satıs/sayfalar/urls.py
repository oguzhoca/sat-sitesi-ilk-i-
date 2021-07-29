
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from sayfalar.views import IndexView, ContactView, OdemeView, AboutView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name="contact"),
    path('ödeme/', OdemeView.as_view(), name="ödeme"),
    path('about/', AboutView.as_view(), name="about"),

]
