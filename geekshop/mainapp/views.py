from django.shortcuts import render
from .models import ProductCategory, Product


def products(request):
    links_menu = [{'href': '', 'name': el.name} for el in ProductCategory.objects.all()]

    context = {
        'title': 'каталог',
        'links_menu': links_menu,
        'object': Product.objects.get(id=1)
    }

    return render(request, 'mainapp/products.html', context=context)
