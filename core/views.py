from django.shortcuts import render
from catalog.models import Product


def home(request):
    best_sellers = Product.objects.order_by(
        '-sold_count',
        '-created_at',)[:5]

    latest_products = Product.objects.order_by('-created_at')[:5]

    return render(request, "core/home.html", {
        "best_sellers": best_sellers,
        "latest_products": latest_products,
    })


def support(request):
    return render(request, "core/support.html")


def page_not_found(request, exception):
    return render(request, '404.html', status=404)