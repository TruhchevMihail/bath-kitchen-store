from django.views.generic import TemplateView
from django.shortcuts import render
from catalog.models import Product


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        best_sellers = Product.objects.order_by('-sold_count', '-created_at')[:5]
        latest_products = Product.objects.order_by('-created_at')[:5]
        context.update({
            'best_sellers': best_sellers,
            'latest_products': latest_products,
        })
        return context


class SupportView(TemplateView):
    template_name = 'core/support.html'


class PageNotFoundView(TemplateView):
    template_name = '404.html'


def page_not_found(request, exception):
    return render(request, '404.html', status=404)
