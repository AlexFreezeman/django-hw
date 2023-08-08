from django.urls import path
from django.views.decorators.cache import cache_page
from catalog.views import home, contacts, ProductsDetailView

app_name = "catalog"

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductsDetailView.as_view(), name='product')
]