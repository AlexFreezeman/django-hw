from django.shortcuts import render
from catalog.models import Product


def home(request):
    products_list = Product.objects.all()
    context = {'object_list': products_list}
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    return render(request, 'catalog/contacts.html')
