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


def products(request, pk):
#    pk = Product.pk
    products_detail = {'object_list': Product.objects.get(pk=pk)}
    return render(request, 'catalog/products.html', products_detail)
#class ProductsDetailView(DetailView):
#    model = Product
#    template_name = 'catalog/products.html'
#    context_object_name = 'item'
#    pk_url_kwarg = 'pk'
