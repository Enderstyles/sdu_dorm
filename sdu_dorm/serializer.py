from rest_framework import serializers

from .models import CustomUser, MainPageModel, NewsPost, NewsCategories, AboutPost, TakenPlaces, PaymentModel, \
    UploadDocumentsModel


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutPost
        fields = '__all__'


class ChangePasswordSerializer(serializers.Serializer):
    student_id = serializers.CharField()
    password = serializers.CharField()

    @staticmethod
    def check_student(value):
        try:
            CustomUser.objects.get(student_id=value)
            return True
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("Student does not exist")

    @staticmethod
    def update_password(validated_data):
        student_id = validated_data.get("student_id")
        password = validated_data.get("password")
        student = CustomUser.objects.get(student_id=student_id)
        student.set_password(password)
        student.save()


class MainPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPageModel
        fields = '__all__'


class NewsObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPost
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPost
        fields = [
                'id',
                'main_image', 'news_title', 'news_description',
                'date_of_the_event', 'time_of_the_event',
                'category_of_the_event', 'place_of_the_event'
        ]


class NewsCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategories
        fields = '__all__'


class TakeASeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = TakenPlaces
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentModel
        fields = '__all__'


class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadDocumentsModel
        fields = '__all__'
