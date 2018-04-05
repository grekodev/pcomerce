from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from comments.forms import CommentForm
from products.models import Product

# Create your views here.


class HomeView(TemplateView):
    template_name = 'products/home.html'

    def get_context_data(self, *args, **kwargs):
        products = Product.objects.all()
        return {'products': products}


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        comment_form = CommentForm()
        return {'comment_form': comment_form}



