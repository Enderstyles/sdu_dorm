from django.contrib import admin

from django.urls import path, include
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from sdu_dorm.views import StudentsViewListApi, AboutPiecesViewApi

router = routers.DefaultRouter()
# router.register(r'api/login', LoginViewListApi)
# router.register(r'api/students', StudentsViewListApi)
# router.register(r'api/about_pieces', AboutPiecesViewApi)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path("api/schema/docs/", SpectacularSwaggerView.as_view(url_name='schema')),
    path('api/profile/', StudentsViewListApi.as_view(), name='profile'),
    path('api/about_pieces/', AboutPiecesViewApi.as_view(), name='about'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
