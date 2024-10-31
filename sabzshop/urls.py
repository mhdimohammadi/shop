from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('shop.urls', namespace='shop')),
    path("cart/", include('cart.urls', namespace='cart')),
    path('order/',include('order.urls',namespace="order"))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
