from django.shortcuts import render

from mainapp.views import get_products


def index(request):
    products = get_products()

    context = {
        'title': 'главная',
        'products': products,
    }

    return render(request, 'geekshop/index.html', context=context)


def contacts(request):
    context = {
        'title': 'контакты',
    }

    return render(request, 'geekshop/contact.html', context=context)
