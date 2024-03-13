from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken

from sdu_dorm.models import CustomUser, AboutPiece, MainPageModel, NewsPost, NewsCategories
from sdu_dorm.serializer import UserInfoSerializer, AboutSerializer, ChangePasswordSerializer, MainPageSerializer, \
    NewsSerializer, NewsCategoriesSerializer


class ProfileApi(ListAPIView):
    serializer_class = UserInfoSerializer

    @extend_schema(responses=UserInfoSerializer)
    def list(self, request, *args, **kwargs):
        queryset = CustomUser.objects.filter(student_id=request.user.student_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AboutPiecesViewApi(ListAPIView):
    serializer_class = AboutSerializer

    @extend_schema(responses=AboutSerializer)
    def list(self, request, *args, **kwargs):
        queryset = AboutPiece.objects.all()
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

    @extend_schema(responses=MainPageSerializer)
    def list(self, request, *args, **kwargs):
        queryset = MainPageModel.objects.all()
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
            return Response(serializer.data)
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

    serializer_class = NewsSerializer
    queryset = NewsPost.objects.all()

    def retrieve(self, request, *args, **kwargs):
        object_id = kwargs.get('pk')  # 'pk' is the default name for the primary key parameter
        try:
            queryset = self.get_queryset().get(id=object_id)
            serializer = self.get_serializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except NewsPost.DoesNotExist:
            return Response({"detail": "Object not found"}, status=status.HTTP_404_NOT_FOUND)


class GetNewsCategoriesApi(RetrieveAPIView):
    permission_classes = (AllowAny,)
    authentication_classes = []

    serializer_class = NewsCategoriesSerializer
    queryset = NewsCategories.objects.all()

    def retrieve(self, request, *args, **kwargs):
        object_id = kwargs.get('pk')  # 'pk' is the default name for the primary key parameter
        try:
            queryset = self.get_queryset().get(id=object_id)
            serializer = self.get_serializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except NewsPost.DoesNotExist:
            return Response({"detail": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
