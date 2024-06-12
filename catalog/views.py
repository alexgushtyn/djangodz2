from django.shortcuts import render
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, TemplateView, DetailView, UpdateView
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


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ('title', 'content', 'preview',)
    success_url = reverse_lazy('catalog:posts')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.is_published = True
            new_post.save()

        return super().form_valid(form)


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'content', 'preview',)

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(new_post.title)
            new_post.is_published = True
            new_post.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:post', args=(self.object.slug,))



class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('catalog:posts')