from django.urls import path
from catalog.views import index, contacts, categories, category_auto
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('categories/', categories, name='categories'),
    path('<int:pk>/catalog/', category_auto, name='category_auto'),
]
