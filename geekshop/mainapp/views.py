import random
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from mainapp.models import ProductCategory, Product
from basketapp.models import Basket


def get_basket(user):
    return Basket.objects.filter(user=user) if user.is_authenticated else []


def get_hot_product():
    products = Product.objects.all()

    return random.sample([products], 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return same_products


def products(request, pk=None):
    print(pk)

    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    basket = get_basket(request.user)

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
            'basket': basket,
        }

        return render(request, 'mainapp/products_list.html', context=context)

    hot_product = get_hot_product()
    same_products = Product.objects.all()[3:5]

    context = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
    }

    return render(request, 'mainapp/products.html', context=context)


def product(request, pk):
    title = 'детали продукта'
    links_menu = ProductCategory.objects.all()
    product = get_object_or_404(Product, pk=pk)
    basket = get_basket(request.user)

    context = {
        'title': title,
        'links_menu': links_menu,
        'product': product,
        'basket': basket,
    }

    return render(request, 'mainapp/product.html', context=context)
