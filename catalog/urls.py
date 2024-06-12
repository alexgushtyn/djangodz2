from django.urls import path
from catalog.views import ProductListView, CategoryListView, ProductListView, ContactTemplateView, ProductDetailView, \
    BlogPostDetailView, BlogPostListView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', ContactTemplateView.as_view(), name='contacts'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('product/<int:pk>/details/', ProductDetailView.as_view(), name='product_details'),
    path('blog/', BlogPostListView.as_view(), name='posts'),
    path('blog/create/', BlogPostCreateView.as_view(), name='create_post'),
    path('blog/update/<int:pk>', BlogPostUpdateView.as_view(), name='update_post'),
    path('blog/<slug>', BlogPostDetailView.as_view(), name='post'),
    path('blog/delete/<int:pk>', BlogPostDeleteView.as_view(), name='delete_post'),

]
