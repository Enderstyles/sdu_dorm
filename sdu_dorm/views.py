from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.response import Response

from sdu_dorm.models import CustomUser, AboutPiece
from sdu_dorm.serializer import UserInfoSerializer, AboutSerializer


class StudentsViewListApi(ListAPIView):
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
