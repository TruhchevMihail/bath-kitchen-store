from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('core.urls')),
    path('bath/', include('catalog.urls')),
    path('kitchen/', include('catalog.urls')),
    path('catalogue/', include('catalog.urls')),
    path('projects/', include('projects.urls')),
    path('cart/', include('shopping_cart.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)