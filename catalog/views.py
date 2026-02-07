from django.shortcuts import render

BATH_CATEGORIES = [
    {"slug": "tiles", "title": "Tiles", "desc": "Wall & floor tiles"},
    {"slug": "faucets", "title": "Faucets", "desc": "Mixers, shower systems"},
    {"slug": "sanitary", "title": "Sanitary Ware", "desc": "Toilets, sinks, basins"},
    {"slug": "showers", "title": "Showers", "desc": "Cabins, screens, drains"},
    {"slug": "furniture", "title": "Bathroom Furniture", "desc": "Vanities, mirrors"},
    {"slug": "accessories", "title": "Accessories", "desc": "Holders, shelves, etc."},
]

KITCHEN_CATEGORIES = [
    {"slug": "sinks", "title": "Kitchen Sinks", "desc": "Granite & inox sinks"},
    {"slug": "faucets", "title": "Kitchen Faucets", "desc": "Pull-out & classic"},
    {"slug": "worktops", "title": "Worktops", "desc": "Oak, compact, stone"},
    {"slug": "backsplash", "title": "Backsplash", "desc": "Panels & tiles"},
    {"slug": "hardware", "title": "Hardware", "desc": "Hinges, handles"},
    {"slug": "lighting", "title": "Lighting", "desc": "LED & task lights"},
]

ALL_CATEGORIES = [
    *BATH_CATEGORIES,
    *KITCHEN_CATEGORIES,
]

def _section_from_path(path: str) -> str:
    if path.startswith("/bath/"):
        return "bath"
    if path.startswith("/kitchen/"):
        return "kitchen"
    return "catalogue"

def catalogue_home(request):
    section = _section_from_path(request.path)

    if section == "bath":
        title = "Bath"
        subtitle = "Shop by bathroom categories"
        categories = BATH_CATEGORIES
    elif section == "kitchen":
        title = "Kitchen"
        subtitle = "Shop by kitchen categories"
        categories = KITCHEN_CATEGORIES
    else:
        title = "Catalogue"
        subtitle = "Browse all categories"
        categories = ALL_CATEGORIES

    return render(request, "catalog/catalogue_home.html", {
        "section": section,
        "title": title,
        "subtitle": subtitle,
        "categories": categories,
    })

def category_detail(request, category_slug):
    section = _section_from_path(request.path)

    #TODO: pull products from DB later
    products = [
        {"title": "Product 1", "price": "12.43", "badge": "NEW"},
    ]

    return render(request, "catalog/category_detail.html", {
        "section": section,
        "category_slug": category_slug,
        "products": products,
    })
