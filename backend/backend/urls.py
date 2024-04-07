from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/register/', CreateUserView.as_view(), name='Register'),
    path('api/token/', TokenObtainPairView.as_view(), name='Get Token'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='Refresh Token'),
    path('api-auth/', include("rest_framework.urls")),
    path('api/', include('api.urls'))
]
