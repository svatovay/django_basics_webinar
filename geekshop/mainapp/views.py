from django.shortcuts import render, get_object_or_404
from mainapp.models import ProductCategory, Product
from basketapp.models import Basket


def products(request, pk=None):
    print(pk)

    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

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

    same_products = Product.objects.all()[3:5]

    context = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
    }

    return render(request, 'mainapp/products.html', context=context)
