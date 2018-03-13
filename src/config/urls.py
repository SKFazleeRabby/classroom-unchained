from django.urls import path, include
from config import settings
from . import views

urlpatterns = [
    path('api/user/', include('app.account.urls'))
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('api/__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

