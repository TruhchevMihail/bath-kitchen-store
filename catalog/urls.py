from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogue_home, name='catalogue_home'),
    path('<slug:category_slug>/', views.category_detail, name='category_detail'),
    #path('product/<slug:product_slug>/', views.product_detail, name='product_detail')
]
