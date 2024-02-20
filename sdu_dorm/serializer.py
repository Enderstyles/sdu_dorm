from rest_framework import serializers

from .models import CustomUser, AboutPiece


# class UserLoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'password']
#         extra_kwargs = {'password': {'write_only': True}}

# def create(self, validated_data):
#     user = CustomUser(
#         username=validated_data['user_id'],
#         email=validated_data['email']
#     )
#     user.set_password(validated_data['password'])
#     user.save()
#     return user


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutPiece
        fields = '__all__'


# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ('user_id', 'password')
#
#
# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = '__all__'
#
#

