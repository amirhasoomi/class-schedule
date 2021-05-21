from django.urls import path, include
from drf_spectacular.views import (SpectacularAPIView,
                                   SpectacularRedocView,
                                   SpectacularSwaggerView)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/', include([
        path('auth/', include('authentication.urls')),
        path('features/', include('features.urls')),
        path('projection/', include('projection.urls')),

    ])),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(
        url_name='schema'), name='swagger-ui'),
    path('redoc', SpectacularRedocView.as_view(
        url_name='schema'), name='redoc'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
