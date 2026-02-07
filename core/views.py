from django.shortcuts import render

def home(request):
    # TODO: replace with real queries after models exist
    best_sellers = [
        {"title": "Best Seller #1", "price": "TODO", "tag": "TOP"},
        {"title": "Best Seller #2", "price": "TODO", "tag": "TOP"},
        {"title": "Best Seller #3", "price": "TODO", "tag": "TOP"},
        {"title": "Best Seller #4", "price": "TODO", "tag": "TOP"},
        {"title": "Best Seller #5", "price": "TODO", "tag": "TOP"},
    ]

    latest_products = [
        {"title": "New Product #1", "price": "TODO", "tag": "NEW"},
        {"title": "New Product #2", "price": "TODO", "tag": "NEW"},
        {"title": "New Product #3", "price": "TODO", "tag": "NEW"},
        {"title": "New Product #4", "price": "TODO", "tag": "NEW"},
        {"title": "New Product #5", "price": "TODO", "tag": "NEW"},
    ]

    return render(request, "core/home.html", {
        "best_sellers": best_sellers,
        "latest_products": latest_products,
    })
