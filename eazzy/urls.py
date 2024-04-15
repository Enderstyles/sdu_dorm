from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from eazzy import settings
from sdu_dorm import views
from sdu_dorm.views import ProfileApi, AboutPiecesViewApi, ForgotPasswordApi, LogoutView, NewsFeedApi, \
    NewsObjectApi, GetNewsCategoriesApi, FollowPostApi, GetAllFollowingPostsApi, TakeAPlaceApi, GetTakenPlacesApi, \
    CreateStudentApi, UnfollowPostApi, PostLink, FailureLink, BackLink, FailureBackLink
from sdu_dorm.views import MainPageApi

router = routers.DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path("api/schema/docs/", SpectacularSwaggerView.as_view(url_name='schema')),
    path('api/profile/', ProfileApi.as_view(), name='profile'),
    path('api/about/', AboutPiecesViewApi.as_view(), name='about'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/forgot_password/', ForgotPasswordApi.as_view(), name='auth_change_password'),
    path('api/logout/', LogoutView.as_view(), name='auth_logout'),
    path('api/main_page/', MainPageApi.as_view(), name='main_page'),
    path('api/news/', NewsFeedApi.as_view(), name='news'),
    path('api/news/<int:pk>/', NewsObjectApi.as_view(), name='news_object_api'),
    path('api/news_categories/', GetNewsCategoriesApi.as_view(), name='news_categories'),
    path('api/follow_post/', FollowPostApi.as_view(), name='follow'),
    path('api/unfollow_post/', UnfollowPostApi.as_view(), name='unfollow'),
    path('api/get_followed_posts/', GetAllFollowingPostsApi.as_view(), name='followed_posts'),
    path('api/take_place/', TakeAPlaceApi.as_view(), name='take_place'),
    path('api/get_taken_places/', GetTakenPlacesApi.as_view(), name='get_taken_places'),
    path('test_celery', views.test, name='test'),
    path('api/create_student/', CreateStudentApi.as_view(), name='create_student'),
    path('api/postlink/', PostLink.as_view(), name='post_link'),
    path('api/failurelink/', FailureLink.as_view(), name='failure_link'),
    path('api/backlink/', BackLink.as_view(), name='back_link'),
    path('api/failure_back_link/', FailureBackLink.as_view(), name='failure_back_link'),
    # path('api/edit_main_page/', EditMainPage.as_view(), name='edit_main_page')
    # path('api/new_student', NewStudentApi.as_view(), name='new_student')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
