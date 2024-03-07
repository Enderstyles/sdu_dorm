from rest_framework import serializers

from .models import CustomUser, AboutPiece, MainPageModel


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutPiece
        fields = '__all__'


class ChangePasswordSerializer(serializers.Serializer):
    student_id = serializers.CharField()
    password = serializers.CharField()

    def check_student(self, value):
        try:
            CustomUser.objects.get(student_id=value)
            return True
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("Student does not exist")

    def update_password(self, validated_data):
        student_id = validated_data.get("student_id")
        password = validated_data.get("password")
        student = CustomUser.objects.get(student_id=student_id)
        student.set_password(password)
        student.save()


class MainPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPageModel
        fields = '__all__'

