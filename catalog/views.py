from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, TemplateView, DetailView
from catalog.models import Product, Category, Contacts, BlogPost



class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'CARUP! Shop',
        'description': 'Вся информация о товаре',
    }



class ContactTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {
        'title': 'Контакты',
        'description': 'Наша контактная информация',
    }



class ProductDetailView(DetailView):
    model = Product


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории'
    }




class BlogPostListView(ListView):
    model = BlogPost



class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object
