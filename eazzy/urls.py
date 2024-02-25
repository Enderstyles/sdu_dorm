"""
URL configuration for eazzy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from sdu_dorm.views import StudentsViewListApi, AboutPiecesViewApi, index

router = routers.DefaultRouter()
# router.register(r'api/login', LoginViewListApi)
# router.register(r'api/students', StudentsViewListApi)
# router.register(r'api/about_pieces', AboutPiecesViewApi)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path("api/schema/docs/", SpectacularSwaggerView.as_view(url_name='schema')),
    # path('login/', LoginViewListApi.as_view(), name="login_list"),
    # path('students/', StudentsViewListApi.as_view(), name="students_list"),
    # path('login/', user_login, name='login'),
    # path('logout/', user_logout, name='logout'),
    # path('register/', register_user, name='register'),
    # path('login/', user_login, name='login'),
    # path('logout/', user_logout, name='logout'),
    path('api/profile/', StudentsViewListApi.as_view(), name='profile'),
    path('api/about_pieces/', AboutPiecesViewApi.as_view(), name='about'),
    # path('test_f/', test_f, name='test_f'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
