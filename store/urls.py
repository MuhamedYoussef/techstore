from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<slug:slug>', views.product, name='product'),
    path('search/', views.search, name='search'),
    path('cart', views.cart, name='cart'),
    path('get_cart_items/', views.get_cart_items, name='get_cart_items'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
