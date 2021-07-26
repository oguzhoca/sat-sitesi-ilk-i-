
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from sayfalar.views import IndexView, ContactView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name="contact"),
]
