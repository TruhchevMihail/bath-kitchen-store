from django.shortcuts import render, get_object_or_404
from .models import Category, Product , Brand


def bath_home(request):
    categories = Category.objects.filter(section=Category.BATH).order_by('title')

    context = {
        'section': 'bath',
        'title': 'Bath',
        'subtitle': 'Our Bathroom Products',
        'categories': categories,
    }

    return render(request, 'catalog/section_home.html', context)


def kitchen_home(request):
    categories = Category.objects.filter(section=Category.KITCHEN).order_by('title')

    context = {
        'section': 'kitchen',
        'title': 'Kitchen',
        'subtitle': 'Our Kitchen Products',
        'categories': categories,
    }

    return render(request, 'catalog/section_home.html', context)


def category_products(request, section, category_slug):
    category = get_object_or_404(Category, slug=category_slug, section=section)

    products = (
        Product.objects
        .filter(category=category)
        .select_related('brand', 'category')
        .order_by('-created_at')
    )

    context = {
        'section': section,
        'category': category,
        'products': products,
    }

    return render(request, 'catalog/category_detail.html', context)


def brand_detail(request, brand_slug):
    brand = get_object_or_404(Brand, slug=brand_slug)

    products = (
        Product.objects
        .filter(brand=brand)
        .select_related('brand', 'category')
        .order_by('-created_at')
    )

    context = {
        'brand': brand,
        'products': products,
    }

    return render(request, "catalog/brand_detail.html", context)


def brand_list(request):
    brands = Brand.objects.all().order_by("name")

    context = {
        "brands": brands,
    }
    return render(request, "catalog/brand_list.html", context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)

    context = {
        'product': product,
    }

    return render(request, 'catalog/product_detail.html', context)