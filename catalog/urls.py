from django.urls import path
from django.views.decorators.cache import cache_page
from catalog.views import contacts, ProductsDetailView, ProductListView, BlogList, BlogDetailView, BlogCreatePost, \
    BlogUpdatePost, BlogDeletePost

app_name = "catalog"

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductsDetailView.as_view(), name='product'),
    path('blog/', BlogList.as_view(), name='blog'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog_post'),
    path('create_post/', BlogCreatePost.as_view(), name='create_post'),
    path('update_post/<slug:slug>/', BlogUpdatePost.as_view(), name='update_post'),
    path('delete_post/<slug:slug>/', BlogDeletePost.as_view(), name='delete_post')
]