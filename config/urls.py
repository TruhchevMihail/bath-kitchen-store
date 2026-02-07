from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('core.urls')),
    path('bath/', include('catalog.urls')),
    path('kitchen/', include('catalog.urls')),
    path('catalogue/', include('catalog.urls')),
    path('projects/', include('projects.urls')),
    path('cart/', include('shopping_cart.urls')),
]
