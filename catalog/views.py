from django.shortcuts import render
from django.views.generic import DetailView

from catalog import models
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

#class ProductsDetailView(DetailView):
#    def product(request, pk):
#        Model = models.Product
#        template_name = 'catalog/products.html'
#        context = super().get_context_data(pk=pk)
#        context['object_list'] = Product.objects.all()
#    pk = Product.pk
#        product_detail = Product.objects.get(pk=pk)
#        product_detail[pk] = pk.objects.first()
#        return context
#    return render(request, 'catalog/products.html', products_detail)
class ProductsDetailView(DetailView):
    model = Product
    template_name = 'catalog/products.html'
    context_object_name = 'product'
