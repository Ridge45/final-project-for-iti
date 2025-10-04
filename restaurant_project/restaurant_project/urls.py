from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', include('menu.urls', namespace='menu')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('customers/', include('customers.urls', namespace='customers')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('', RedirectView.as_view(pattern_name='menu:item_list', permanent=False)),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
