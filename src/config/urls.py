from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
from config import settings

urlpatterns = [
    path('api/jwt/authentication/', obtain_jwt_token),
    path('api/jwt/verification/', verify_jwt_token),
    path('api/jwt/refresh/token', refresh_jwt_token),
    path('api/api-auth/', include('rest_framework.urls')),
    path('api/user/', include('app.account.urls')),
    path('api/classroom/', include('app.classroom.urls')),
    path('api/post/', include('app.post.urls'))
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('api/__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
