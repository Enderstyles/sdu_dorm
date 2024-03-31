import datetime

from django.http import HttpResponse
from django.utils import timezone
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from sdu_dorm.models import CustomUser, MainPageModel, NewsPost, NewsCategories, AboutPost, Enrollment, \
    TakenPlace
from sdu_dorm.serializer import UserInfoSerializer, AboutSerializer, ChangePasswordSerializer, MainPageSerializer, \
    NewsSerializer, NewsCategoriesSerializer, NewsObjectSerializer, TakeASeatSerializer

from .tasks import test_task, check_event


def test(request):
    check_event.delay()
    return HttpResponse("Done")


class ProfileApi(ListAPIView):
    serializer_class = UserInfoSerializer

    def list(self, request, *args, **kwargs):
        queryset = CustomUser.objects.filter(student_id=request.user.student_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AboutPiecesViewApi(ListAPIView):
    permission_classes = (AllowAny,)
    authentication_classes = []
    serializer_class = AboutSerializer

    def list(self, request, *args, **kwargs):
        queryset = AboutPost.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ForgotPasswordApi(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = []

    @staticmethod
    def post(request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data)
        if not serializer.is_valid():
            print("serializer ", serializer)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if not serializer.check_student(request.data['student_id']):
            print("no such student")
            return Response({'message': 'Does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        serializer.update_password(serializer.validated_data)
        return Response({'success': 'Password has been changed'}, status=status.HTTP_200_OK)


class LogoutView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = []

    @staticmethod
    def post(request, *args, **kwargs):
        try:
            print("aa")
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        finally:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class MainPageApi(ListAPIView):
    permission_classes = (AllowAny,)
    authentication_classes = []
    serializer_class = MainPageSerializer

    def list(self, request, *args, **kwargs):
        queryset = MainPageModel.objects.filter(id=1)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EditMainPage(APIView):
    queryset = MainPageModel.objects.get(id=1)
    serializer_class = MainPageSerializer

    def put(self, request, *args, **kwargs):
        instance = self.queryset
        serializer = MainPageSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsFeedApi(ListAPIView):
    permission_classes = (AllowAny,)
    authentication_classes = []

    serializer_class = NewsSerializer

    def list(self, request, *args, **kwargs):
        queryset = NewsPost.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NewsObjectApi(RetrieveAPIView):
    permission_classes = (AllowAny,)
    authentication_classes = []

    serializer_class = NewsObjectSerializer
    queryset = NewsPost.objects.all()

    def retrieve(self, request, *args, **kwargs):
        object_id = kwargs.get('pk')  # 'pk' is the default name for the primary key parameter
        try:
            queryset = self.get_queryset().get(id=object_id)
            serializer = self.get_serializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except NewsPost.DoesNotExist:
            return Response({"detail": "Object not found"}, status=status.HTTP_404_NOT_FOUND)


# class GetNewsCategoriesApi(RetrieveAPIView):
#     permission_classes = (AllowAny)
#     authentication_classes = []
#
#     serializer_class = NewsCategoriesSerializer
#     queryset = NewsCategories.objects.all()
#
#     def retrieve(self, request, *args, **kwargs):
#         object_id = kwargs.get('pk')  # 'pk' is the default name for the primary key parameter
#         try:
#             queryset = self.get_queryset().get(id=object_id)
#             serializer = self.get_serializer(queryset)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except NewsPost.DoesNotExist:
#             return Response({"detail": "Object not found"}, status=status.HTTP_404_NOT_FOUND)

class GetNewsCategoriesApi(ListAPIView):
    permission_classes = (AllowAny,)
    authentication_classes = []
    serializer_class = NewsCategoriesSerializer

    def list(self, request, *args, **kwargs):
        queryset = NewsCategories.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FollowPostApi(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = []

    @staticmethod
    def post(request, *args, **kwargs):
        try:
            follower_id = request.data["student_id"]
            post_id = request.data["post_id"]

            student = CustomUser.objects.get(student_id=follower_id)
            post = NewsPost.objects.get(id=post_id)
            if Enrollment.objects.filter(student_id=student, post=post).exists():
                return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)

            Enrollment.objects.create(student_id=student, post=post, date=datetime.datetime.now())
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GetAllFollowingPostsApi(ListAPIView):
    serializer_class = NewsSerializer

    def list(self, request, *args, **kwargs):
        user = CustomUser.objects.get(student_id=request.user.student_id)
        all_posts = user.follows.all().values_list("id")
        print(all_posts)
        queryset = NewsPost.objects.filter(id__in=all_posts)
        serializer = NewsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetTakenPlacesApi(ListAPIView):
    permission_classes = (AllowAny,)
    authentication_classes = []
    serializer_class = TakeASeatSerializer

    def get_queryset(self):
        return TakenPlace.objects.all()


class TakeAPlaceApi(APIView):
    serializer_class = TakeASeatSerializer

    @staticmethod
    def post(request, *args, **kwargs):
        try:
            student_id = request.data["student_id"]
            place = request.data["place"]
            student = CustomUser.objects.get(student_id=student_id)

            if TakenPlace.objects.get(place=place).exists():
                return Response(status=status.HTTP_409_CONFLICT)

            TakenPlace.objects.create(place=place, taken_by=student)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
