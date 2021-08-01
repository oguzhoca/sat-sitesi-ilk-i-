from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from items.models import Item, Category, Tag


class ItemListView(ListView):
    model = Item
    template_name = 'items.html'
    context_object_name = 'items'

   

class ItemDetailView(DetailView):
    model = Item
    template_name = 'item.html'
    context_object_name = 'item'

def category_list(request, category_slug):
    items = Item.objects.all().filter(category__slug=category_slug)
    categories = Category.objects.all()
    tags= Tag.objects.all()

    context = {
        'items': items,
        'categories': categories,
        'tags':tags,
        'category':Category
    }

    return render(request, 'items.html', context)

    