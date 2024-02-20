from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from drf_spectacular.utils import extend_schema
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from sdu_dorm.models import CustomUser, AboutPiece
from sdu_dorm.serializer import UserInfoSerializer, AboutSerializer


# @api_view(['POST'])
# def register_user(request):
#     if request.method == 'POST':
#
#         serializer = UserLoginSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def user_info(request):
#     if request.method == 'GET':
#         serializer = UserInfoSerializer(request.user)
#         return Response(serializer.data, status=status.HTTP_302_FOUND)
#
#
# @api_view(['GET'])
# def test_f(request):
#     if request.method == 'GET':
#         # Pass the user instance to the serializer
#         serializer = UserInfoSerializer(request.user)
#         user = CustomUser.objects.get(username='medokser')
#         print(user)
#         token, _ = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key, }, status=status.HTTP_200_OK)
#     return Response({'error: error'}, status=status.HTTP_400_BAD_REQUEST)
#
#
# # @api_view(['POST'])
# # def user_login(request):
# #     if request.method == 'POST':
# #         username = request.data.get('username')
# #         password = request.data.get('password')
# #
# #         user = None
# #         if '@' in username:
# #             try:
# #                 user = CustomUser.objects.get(email=username)
# #             except ObjectDoesNotExist:
# #                 pass
# #
# #         if not user:
# #             user = authenticate(username=username, password=password)
# #
# #         if user:
# #             token, _ = Token.objects.get_or_create(user=user)
# #             return Response({'token': token.key}, status=status.HTTP_200_OK)
# #
# #         return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#
#
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def user_logout(request):
#     if request.method == 'POST':
#         try:
#             # Delete the user's token to logout
#             request.user.auth_token.delete()
#             return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#


# ------------old------------------

# class LoginViewListApi(ListAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class =
#
#     # @extend_schema(responses=StudentSerializer)
#     # def list(self, request, *args, **kwargs):
#     #     serializer = self.get_serializer(self.queryset, many=True)
#     #     return JsonResponse(serializer.data, safe=False)


class StudentsViewListApi(ListAPIView):
    serializer_class = UserInfoSerializer

    @extend_schema(responses=UserInfoSerializer)
    def list(self, request, *args, **kwargs):
        queryset = CustomUser.objects.filter(username=request.user.username)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AboutPiecesViewApi(ListAPIView):
    serializer_class = AboutSerializer

    @extend_schema(responses=AboutSerializer)
    def list(self, request, *args, **kwargs):
        queryset = AboutPiece.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
