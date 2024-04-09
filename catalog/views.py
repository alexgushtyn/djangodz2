from django.shortcuts import render

from catalog.models import Product, Category


def index(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'CARUP! Shop',
        'description': 'Вся информация о товаре',
    }

    return render(request, 'catalog/index.html', context)


def contacts(request):
    context = {
        'title': 'Контакты',
        'description': 'Наша контактная информация',
    }
    return render(request, 'catalog/contacts.html', context)


def categories(request):

    context = {
        'object_list': Category.objects.all(),
        'title': 'Категории',
    }

    return render(request, 'catalog/categories.html', context)


def category_auto(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'object': product,
        'title': f'Все товары {product.name}'
    }

    return render(request, 'catalog/products.html', context)
