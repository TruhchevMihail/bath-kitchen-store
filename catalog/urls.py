from django.urls import path
from . import views
from .views import product_detail

bath_patterns = [
    path("bath/", views.bath_home, name="bath_home"),
    path("bath/<slug:category_slug>/", views.category_products, {"section": "bath"}, name="bath_category"),
]

kitchen_patterns = [
    path("kitchen/", views.kitchen_home, name="kitchen_home"),
    path("kitchen/<slug:category_slug>/", views.category_products, {"section": "kitchen"}, name="kitchen_category"),
]

category_patterns = [
    path("categories/", views.CategoryListView.as_view(), name="category_list"),
    path("categories/create/", views.CategoryCreateView.as_view(), name="category_create"),
    path("categories/<slug:slug>/edit/", views.CategoryUpdateView.as_view(), name="category_edit"),
    path("categories/<slug:slug>/delete/", views.CategoryDeleteView.as_view(), name="category_delete"),
    path("categories/<slug:slug>/", views.CategoryDetailView.as_view(), name="category_detail"),
]

product_patterns = [
    path("products/", views.ProductListView.as_view(), name="product_list"),
    path("products/create/", views.ProductCreateView.as_view(), name="product_create"),
    path("products/<slug:slug>/edit/", views.ProductUpdateView.as_view(), name="product_edit"),
    path("products/<slug:slug>/delete/", views.ProductDeleteView.as_view(), name="product_delete"),
    path("products/<slug:slug>/", product_detail, name="product_detail"),
]

catalogue_patterns = [
    path("catalogue/", views.brand_list, name="brand_list"),
    path("catalogue/create/", views.BrandCreateView.as_view(), name="brand_create"),
    path("catalogue/<slug:brand_slug>/edit/", views.BrandUpdateView.as_view(), name="brand_edit"),
    path("catalogue/<slug:brand_slug>/delete/", views.BrandDeleteView.as_view(), name="brand_delete"),
    path("catalogue/<slug:brand_slug>/", views.brand_detail, name="brand_detail"),
]

urlpatterns = [
    *bath_patterns,
    *kitchen_patterns,
    *product_patterns,
    *catalogue_patterns,
    *category_patterns,
]