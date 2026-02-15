from django.core.paginator import Paginator
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .forms import ProductCreateForm, ProductUpdateForm, BrandCreateForm, BrandUpdateForm, CategoryCreateForm, \
    CategoryUpdateForm
from .models import Category, Product , Brand


class SectionHomeView(ListView):
    model = Product
    template_name = 'catalog/section_home.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_section(self):
        return self.kwargs.get('section')

    def get_queryset(self):
        section = self.get_section()
        qs = Product.objects.filter(category__section=section).select_related('brand', 'category')

        q = (self.request.GET.get('q') or '').strip()
        if q:
            if len(q) < 2:
                return qs.none()
            qs = qs.filter(
                models.Q(title__icontains=q) |
                models.Q(unique_id__icontains=q) |
                models.Q(brand__name__icontains=q) |
                models.Q(category__title__icontains=q)
            ).distinct()

        sort = self.request.GET.get('sort', 'newest')
        valid_sorts = {
            'price': 'price',
            '-price': '-price',
            'title': 'title',
            '-title': '-title',
            'newest': '-created_at',
            'oldest': 'created_at',
        }
        db_sort = valid_sorts.get(sort, '-created_at')
        return qs.order_by(db_sort)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        section = self.get_section()
        categories = Category.objects.filter(section=section).order_by('title')

        if section == Category.BATH:
            title = 'Bath'
            subtitle = 'Our Bathroom Products'
        else:
            title = 'Kitchen'
            subtitle = 'Our Kitchen Products'

        context.update({
            'section': section,
            'title': title,
            'subtitle': subtitle,
            'categories': categories,
            'current_sort': self.request.GET.get('sort', 'newest'),
        })
        return context


class CategoryProductsView(ListView):
    model = Product
    template_name = 'catalog/category_detail.html'
    context_object_name = 'products'
    paginate_by = 12

    def dispatch(self, request, *args, **kwargs):
        self.section = kwargs.get('section')
        self.category = get_object_or_404(Category, slug=kwargs.get('category_slug'), section=self.section)
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs = Product.objects.filter(category=self.category).select_related('brand', 'category')

        q = (self.request.GET.get('q') or '').strip()
        if q:
            if len(q) < 2:
                return qs.none()
            qs = qs.filter(
                models.Q(title__icontains=q) |
                models.Q(unique_id__icontains=q) |
                models.Q(brand__name__icontains=q)
            ).distinct()

        sort = self.request.GET.get('sort', 'newest')
        valid_sorts = {
            'price': 'price',
            '-price': '-price',
            'title': 'title',
            '-title': '-title',
            'newest': '-created_at',
            'oldest': 'created_at',
        }
        db_sort = valid_sorts.get(sort, '-created_at')
        return qs.order_by(db_sort)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'section': self.section,
            'category': self.category,
            'current_sort': self.request.GET.get('sort', 'newest'),
        })
        return context


class BrandListView(ListView):
    model = Brand
    template_name = 'catalog/brand_list.html'
    context_object_name = 'brands'
    paginate_by = 12

    def get_queryset(self):
        qs = Brand.objects.all()
        q = (self.request.GET.get('q') or '').strip()
        if q:
            if len(q) < 2:
                return qs.none()
            qs = qs.filter(name__icontains=q)

        sort = self.request.GET.get('sort', 'name')
        valid_sorts = {
            'name': 'name',
            '-name': '-name',
            'newest': '-id',
            'oldest': 'id',
        }
        db_sort = valid_sorts.get(sort, 'name')
        return qs.order_by(db_sort)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_sort'] = self.request.GET.get('sort', 'name')
        return context


class BrandDetailView(DetailView):
    model = Brand
    template_name = 'catalog/brand_detail.html'
    slug_url_kwarg = 'brand_slug'
    context_object_name = 'brand'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = self.object

        products_list = Product.objects.filter(brand=brand).select_related('brand', 'category')

        q = (self.request.GET.get('q') or '').strip()
        if q:
            if len(q) < 2:
                products_list = products_list.none()
            else:
                products_list = products_list.filter(
                    models.Q(title__icontains=q) |
                    models.Q(unique_id__icontains=q) |
                    models.Q(category__title__icontains=q)
                ).distinct()

        sort = self.request.GET.get('sort', 'newest')
        valid_sorts = {
            'price': 'price',
            '-price': '-price',
            'title': 'title',
            '-title': '-title',
            'newest': '-created_at',
            'oldest': 'created_at',
        }
        db_sort = valid_sorts.get(sort, '-created_at')

        paginator = Paginator(products_list.order_by(db_sort), 12)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context.update({
            'products': page_obj,
            'page_obj': page_obj,
            'is_paginated': page_obj.has_other_pages(),
            'current_sort': sort,
        })
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'product'


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self):
        qs = super().get_queryset()
        
        section = self.request.GET.get('section')
        if section in [Category.BATH, Category.KITCHEN]:
            qs = qs.filter(category__section=section)

        category_id = self.request.GET.get('category')
        if category_id:
            qs = qs.filter(category_id=category_id)

        brand_id = self.request.GET.get('brand')
        if brand_id:
            qs = qs.filter(brand_id=brand_id)

        q = (self.request.GET.get('q') or '').strip()
        if q:
            if len(q) < 2:
                qs = qs.none()
            else:
                qs = qs.filter(
                    models.Q(title__icontains=q) |
                    models.Q(unique_id__icontains=q) |
                    models.Q(brand__name__icontains=q) |
                    models.Q(category__title__icontains=q)
                ).distinct()

        sort = self.request.GET.get('sort', '-created_at')
        valid_sorts = {
            'price': 'price',
            '-price': '-price',
            'title': 'title',
            '-title': '-title',
            'newest': '-created_at',
            'oldest': 'created_at',
        }
        
        db_sort = valid_sorts.get(sort, '-created_at')
        return qs.order_by(db_sort)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_section'] = self.request.GET.get('section')
        context['current_category'] = self.request.GET.get('category')
        context['current_brand'] = self.request.GET.get('brand')
        context['current_sort'] = self.request.GET.get('sort', 'newest')
        
        context['brands'] = Brand.objects.all().order_by('name')
        
        categories_qs = Category.objects.all().order_by('section', 'title')
        if context['current_section']:
            categories_qs = categories_qs.filter(section=context['current_section'])
        context['all_categories'] = categories_qs
        
        context['sections'] = Category.SECTION_CHOICES
        
        return context



class ProductCreateView(CreateView):
    model= Product
    form_class = ProductCreateForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('product_list')

    def get_initial(self):
        initial = super().get_initial()
        category_id = self.request.GET.get('category')
        if category_id:
            initial['category'] = category_id
        
        brand_id = self.request.GET.get('brand')
        if brand_id:
            initial['brand'] = brand_id
            
        return initial


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductUpdateForm
    template_name ='catalog/product_form.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name ='catalog/product_form.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('product_list')


class BrandCreateView(CreateView):
    model = Brand
    form_class = BrandCreateForm
    template_name = 'catalog/brand_form.html'
    success_url = reverse_lazy('brand_list')


class BrandUpdateView(UpdateView):
    model = Brand
    form_class = BrandUpdateForm
    template_name = "catalog/brand_form.html"
    slug_field = "slug"
    slug_url_kwarg = "brand_slug"
    success_url = reverse_lazy("brand_list")


class BrandDeleteView(DeleteView):
    model = Brand
    template_name = 'catalog/brand_confirm_delete.html'
    slug_field = 'slug'
    slug_url_kwarg = 'brand_slug'
    success_url = reverse_lazy('brand_list')


class CategoryListView(ListView):
    model = Category
    template_name = "catalog/category_list.html"
    context_object_name = "categories"
    paginate_by = 12


class CategoryDetailView(DetailView):
    model = Category
    template_name = "catalog/category_detail.html"
    context_object_name = "category"
    slug_field = "slug"
    slug_url_kwarg = "slug"


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryCreateForm
    template_name = "catalog/category_form.html"
    success_url = reverse_lazy("category_list")


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryUpdateForm
    template_name = "catalog/category_form.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    success_url = reverse_lazy("category_list")


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "catalog/category_confirm_delete.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    success_url = reverse_lazy("category_list")