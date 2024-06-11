from django.urls import path
from catalog.views import ProductListView, CategoryListView, ProductListView, ContactTemplateView, ProductDetailView, \
    BlogPostDetailView, BlogPostListView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', ContactTemplateView.as_view(), name='contacts'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('product/<int:pk>/details/', ProductDetailView.as_view(), name='product_details'),
    path('blog/', BlogPostListView.as_view(), name='posts'),
    path('blog/<slug>', BlogPostDetailView.as_view(), name='post'),

]
