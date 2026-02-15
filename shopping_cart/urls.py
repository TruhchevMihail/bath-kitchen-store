from django.urls import path
from . import views

urlpatterns = [
    path('', views.CartView.as_view(), name='cart'),
    path('add/<slug:slug>/', views.AddToCartView.as_view(), name='cart_add'),
    path('remove/<int:product_id>/', views.RemoveFromCartView.as_view(), name='cart_remove'),
    path('update/', views.UpdateCartView.as_view(), name='cart_update'),
    path('clear/', views.ClearCartView.as_view(), name='cart_clear'),
    path('checkout/', views.CheckoutView.as_view(), name='cart_checkout'),
]