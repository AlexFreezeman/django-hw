from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from catalog.models import Product, Blog, Version
from catalog.forms import ProductForm, VersionForm


class ProductListView(ListView):
    model = Product
    context = {'title': 'Список товаров'}
    template_name = 'catalog/home.html'


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


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm

    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        ParentFormset = inlineformset_factory(self.model, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            formset = ParentFormset(self.request.POST, instance=self.object)
        else:
            formset = ParentFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        with transaction.atomic():
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()

        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse('catalog:version', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')


class VersionListView(ListView):
    model = Version

    def get_queryset(self, *args, **kwargs):
        product_pk = self.kwargs.get('pk')
        return Version.objects.filter(is_active=True, product_id=product_pk)

    def get_context_data(self, *args, object_list=None, **kwargs):
        product = Product.objects.get(pk=self.kwargs.get('pk'))
        context = super().get_context_data(*args, **kwargs)
        context['product_title'] = product.title
        context['pk'] = product.pk
        return context
