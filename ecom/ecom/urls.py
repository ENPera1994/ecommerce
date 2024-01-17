
from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('cart/', include('cart.urls')),
    path('procesar_pago/', include('procesar_pago_mp.html')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
