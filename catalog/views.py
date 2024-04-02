from django.shortcuts import render

from catalog.models import Product

def index(request):
    for product_item in Product.objects.all().order_by('-pk')[:5]:
        print(product_item)

    return render(request, 'catalog/index.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    return render(request, 'catalog/contacts.html')
