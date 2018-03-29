from django.urls import path
app_name = 'products'
from products.views import HomeView, ProductDetailView
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name="product"),
]
