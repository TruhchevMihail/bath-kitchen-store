from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_view, name='cart'),
    path('add/<slug:slug>/', views.add_to_cart, name='cart_add'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='cart_remove'),
    path('update/', views.update_cart, name='cart_update'),
    path('clear/', views.clear_cart, name='cart_clear'),
    path('checkout/', views.cart_checkout, name='cart_checkout'),
]