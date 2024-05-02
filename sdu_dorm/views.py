import datetime
import time
import requests

from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.utils.crypto import get_random_string


from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from sdu_dorm.models import CustomUser, MainPageModel, NewsPost, NewsCategories, AboutPost, Enrollment, \
    TakenPlaces, PaymentModel, UploadDocumentsModel
from sdu_dorm.serializer import UserInfoSerializer, AboutSerializer, ChangePasswordSerializer, MainPageSerializer, \
    NewsSerializer, NewsCategoriesSerializer, NewsObjectSerializer, TakeASeatSerializer, DocumentsSerializer

from .tasks import check_event


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
        return Response({'message': 'Password has been changed'}, status=status.HTTP_200_OK)


class LogoutView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = []

    @staticmethod
    def post(request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"message": "Success"}, status=status.HTTP_205_RESET_CONTENT)
        finally:
            return Response({"message": "Unexpected error"}, status=status.HTTP_400_BAD_REQUEST)


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
            return Response({"message": "Object not found"}, status=status.HTTP_404_NOT_FOUND)


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
                return Response({"message": "Already followed"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

            Enrollment.objects.create(student_id=student, post=post, date=datetime.datetime.now())
            return Response({"message": "Success"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)


class UnfollowPostApi(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = []

    @staticmethod
    def post(request, *args, **kwargs):
        try:
            student_id = request.data["student_id"]
            post_id = request.data["post_id"]

            student = CustomUser.objects.get(student_id=student_id)
            post = NewsPost.objects.get(id=post_id)
            enrollment = Enrollment.objects.filter(student_id=student, post=post)
            if enrollment.exists():
                enrollment.delete()
            return Response({"message": "Success"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)


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
        return TakenPlaces.objects.all()


class PaymentApi(ListAPIView):
    def get(self, request, *args, **kwargs):
        grant_type = "client_credentials"
        scope = "payment"
        client_id = "test"
        client_secret = "yF587AV9Ms94qN2QShFzVR3vFnWkhjbAK3sG"
        invoice_id = generate_invoice_id()
        while PaymentModel.objects.filter(invoiceID=invoice_id).exists():
            invoice_id = generate_invoice_id()
        amount = 470000
        currency = "KZT"
        terminal = "67e34d63-102f-4bd1-898e-370781d0074d"

        url = 'https://testoauth.homebank.kz/epay2/oauth2/token'
        body = {
            "grant_type": grant_type,
            "scope": scope,
            "client_id": client_id,
            "client_secret": client_secret,
            "invoiceID": invoice_id,
            "amount": amount,
            "currency": currency,
            "terminal": terminal
        }
        r = requests.request(method='POST', url=url, data=body)
        content = r.json()
        auth = content['access_token']

        student = CustomUser.objects.get(student_id=request.user.student_id)
        PaymentModel.objects.create(invoiceID=invoice_id, token=auth, amount=amount, student=student)
        return Response({
            "message": "Successfully created",
            "response_data": content,
            "invoiceID": invoice_id,
            "amount": amount,
        }, status=status.HTTP_201_CREATED)


class MakeReservation(APIView):
    serializer_class = TakeASeatSerializer

    @staticmethod
    def post(request, *args, **kwargs):
        try:
            student_id = request.data["taken_by_id"]
            block = request.data["block"]
            floor = request.data["floor"]
            taraf = request.data["taraf"]
            room_id = request.data["room"]
            place = request.data["place"]

            taken_by = CustomUser.objects.get(student_id=student_id)

            if TakenPlaces.objects.filter(taken_by_id=taken_by).exists():
                return Response({"message": "User already applied for place"}, status=status.HTTP_409_CONFLICT)
            if TakenPlaces.objects.filter(block=block,
                                          floor=floor,
                                          taraf=taraf,
                                          room=room_id,
                                          place=place).exists():
                return Response({"message": "Place is already taken"}, status=status.HTTP_409_CONFLICT)

            payment = PaymentModel.objects.filter(student=taken_by).last()
            TakenPlaces.objects.create(block=block, floor=floor, taraf=taraf, room=room_id, place=place,
                                       taken_by_id=taken_by, payment=payment.invoiceID)
            return Response({"message": "Success"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)


class CancelReservationApi(APIView):
    @staticmethod
    def post(request, *args, **kwargs):
        student = CustomUser.objects.get(student_id=request.user.student_id)
        if TakenPlaces.objects.filter(taken_by=student).exists():
            TakenPlaces.objects.get(taken_by=student).delete()
            return Response({"message": "success"}, status=status.HTTP_200_OK)
        return Response({"message": "Student didn't take place"}, status=status.HTTP_404_NOT_FOUND)


def generate_invoice_id():
    return get_random_string(15, "0123456789")


class CreateStudentApi(CreateAPIView):
    def post(self, request, *args, **kwargs):
        try:
            serializer = UserInfoSerializer(data=request.data)
            if serializer.is_valid() and CustomUser.objects.filter(student_id=serializer.validated_data["student_id"]):
                password = make_password(serializer.validated_data.get("password"))
                serializer.validated_data["last_login"] = time.strftime('%Y-%m-%d %H:%M:%S')
                serializer.validated_data["date_joined"] = time.strftime('%Y-%m-%d %H:%M:%S')
                serializer.validated_data["email"] = str(serializer.validated_data["student_id"]) + "@stu.sdu.edu.kz"
                serializer.validated_data["is_active"] = True
                serializer.validated_data["password"] = password

                serializer.save()
                return Response({"message": "Successfully created!"}, status=status.HTTP_201_CREATED)
            return Response({"message": "User already exists"}, status.HTTP_409_CONFLICT)
        except Exception as e:
            return Response({"message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)


class PostLink(APIView):
    @staticmethod
    def post(request, *args, **kwargs):
        print(request.data)
        return Response(status=status.HTTP_200_OK)


class FailureLink(APIView):
    @staticmethod
    def post(request, *args, **kwargs):
        print(request.data)
        return Response(status=status.HTTP_200_OK)


class BackLink(APIView):
    @staticmethod
    def post(request, *args, **kwargs):
        print(request.data)
        return Response(status=status.HTTP_200_OK)


class FailureBackLink(APIView):
    @staticmethod
    def post(request, *args, **kwargs):
        print(request.data)
        return Response(status=status.HTTP_200_OK)


class UploadDocumentsApi(APIView):
    @staticmethod
    def post(request, *args, **kwargs):
        try:
            student = CustomUser.objects.get(student_id=request.data["student_id"])
            if UploadDocumentsModel.objects.filter(student=student).exists():
                return Response({"message": "already uploaded"}, status=status.HTTP_409_CONFLICT)
            application = request.FILES["application"]
            photo = request.FILES["photo"]
            identity_card = request.FILES["identity_card"]
            form_075 = request.FILES["form_075"]
            payment_check = request.FILES["payment_check"]
            power_of_attorney = request.FILES["power_of_attorney"]
            address_certificate = request.FILES["address_certificate"]
            university_admission_form = request.FILES["university_admission_form"]

            UploadDocumentsModel.objects.create(student=student,
                                                application=application,
                                                photo=photo,
                                                identity_card=identity_card,
                                                form_075=form_075,
                                                payment_check=payment_check,
                                                power_of_attorney=power_of_attorney,
                                                address_certificate=address_certificate,
                                                university_admission_form=university_admission_form)
            return Response({"message": "Success"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)


class GetDocumentsApi(ListAPIView):
    def get(self, request, *args, **kwargs):
        student = CustomUser.objects.get(student_id=request.user.student_id)
        try:
            if UploadDocumentsModel.objects.filter(student=student).exists():
                data = UploadDocumentsModel.objects.get(student=student)
                serializer = DocumentsSerializer(data)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"message": "not uploaded"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)