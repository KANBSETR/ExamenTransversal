
from django.contrib import admin
from django.urls import path, include
from . import views_token

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    #TokenVerifyView,
)

from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('hotelVeranum.api.urls')),
    
    # Video de donde lo saque: https://www.youtube.com/watch?v=zzBO8qRq_K4
    path('apix/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('apix/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('apix/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
