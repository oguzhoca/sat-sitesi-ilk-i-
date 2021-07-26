from django.urls import path
from items.views import ItemListView, ItemDetailView


urlpatterns = [
    path('', ItemListView.as_view(), name="items"),
    path('item/<int:pk>', ItemDetailView.as_view(), name="item_detail"),
]