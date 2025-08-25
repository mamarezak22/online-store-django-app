from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, AuthUser
from rest_framework_simplejwt.tokens import Token
from rest_framework import serializers

from Users.validators import PhoneNumberValidator

from .models import User


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: AuthUser) -> Token:
        token = super().get_token(user)
        token["phone_number"] = user.phone_number
        return token

class GetCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length = 12,validators = [PhoneNumberValidator,])

class CheckCodeSerializer(serializers.Serializer):
    phone_number =  serializers.CharField(max_length = 12) 
    code = serializers.IntegerField()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "phone_number", "password",)
        extra_kwargs = {"password": {"write_only": True}}

    #so when you said something like user.save()
    #it triggers the createuser function.
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class ChangePasswordSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(max_length = 12)
    code = serializers.IntegerField()
    new_password = serializers.CharField()