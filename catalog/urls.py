from django.urls import path
from . import views
from .views import product_detail

urlpatterns = [
    path('products/<slug:slug>/', product_detail, name='product_detail'),

    path("bath/", views.bath_home, name="bath_home"),
    path("bath/<slug:category_slug>/", views.category_products, {"section": "bath"}, name="bath_category"),

    path("kitchen/", views.kitchen_home, name="kitchen_home"),
    path("kitchen/<slug:category_slug>/", views.category_products, {"section": "kitchen"}, name="kitchen_category"),

    path("catalogue/", views.brand_list, name="brand_list"),
    path("catalogue/<slug:brand_slug>/", views.brand_detail, name="brand_detail"),
]
