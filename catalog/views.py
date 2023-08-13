from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from catalog import models
from catalog.models import Product, Blog


class ProductListView(ListView):
    model = Product
    context = {'title': 'Список товаров'}
    template_name = 'catalog/home.html'


# def home(request):
#    products_list = Product.objects.all()
#    context = {'object_list': products_list}
#    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    return render(request, 'catalog/contacts.html')


class ProductsDetailView(DetailView):
    model = Product
    template_name = 'catalog/products.html'
    context_object_name = 'product'


class BlogList(ListView):
    """Класс-контроллер для страницы со списком постов блога"""
    model = Blog
    extra_context = {'title': 'Блог'}

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        object = super().get_object()
        object.views_count += 1

        object.save()

        return object


class BlogCreatePost(CreateView):
    model = Blog
    fields = ('title', 'content', 'image', 'is_published')
    success_url = '/blog/'


class BlogUpdatePost(UpdateView):
    model = Blog
    fields = ('title', 'content', 'image', 'is_published')

    def get_success_url(self, *args, **kwargs):
        slug = self.kwargs['slug']
        url = reverse_lazy('catalog:blog_post', args=[slug])

        return url


class BlogDeletePost(DeleteView):
    model = Blog
    success_url = '/blog/'
