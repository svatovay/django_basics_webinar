from django.shortcuts import render


def products(request):
    links_menu = {
        'links_menu': [
            {'href': '', 'name': 'все'},
            {'href': '', 'name': 'дом'},
            {'href': '', 'name': 'офис'},
            {'href': '', 'name': 'модерн'},
            {'href': '', 'name': 'классика'}]
    }

    return render(request, 'mainapp/products.html', context=links_menu)
