import random
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.cache import cache
from django.conf import settings
from mainapp.models import ProductCategory, Product


def get_links_menu():
    if settings.LOW_CACHE:
        key = 'links_menu'
        links_menu = cache.get(key)
        if links_menu is None:
            links_menu = ProductCategory.objects.filter(is_active=True)
            cache.set(key, links_menu)
        return links_menu
    else:
        return ProductCategory.objects.filter(is_active=True)


def get_hot_product():
    products = Product.objects.all()

    return random.sample([products], 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return same_products


def products(request, pk=None, page=1):
    title = "Каталог"
    links_menu = get_links_menu()
    products = Product.objects.all().order_by('price')

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        context = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
        }

        return render(request, 'mainapp/products.html', context)

    hot_product = get_hot_product()
    same_product = Product.objects.all()[3:5]

    paginator = Paginator(products, 2)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context = {
        'title': title,
        'links_menu': links_menu,
        'products': products_paginator,
        'hot_product': hot_product,
        'same_products': same_product,
    }

    return render(request, 'mainapp/products.html', context=context)


def product(request, pk):
    title = 'детали продукта'
    links_menu = get_links_menu()
    product = get_object_or_404(Product, pk=pk)

    # hot_product = get_hot_product()
    same_product = Product.objects.all()[3:5]

    context = {
        'title': title,
        'links_menu': links_menu,
        'product': product,
        'same_products': same_product,
    }

    return render(request, 'mainapp/product.html', context=context)
