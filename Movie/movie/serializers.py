from rest_framework import serializers
from .models import User_Details,Movie_Details,Movie_Booking
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from django.contrib.auth import get_user_model

User = get_user_model()


class UserLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True, max_length=100)
    username = serializers.CharField(required=True, write_only=True, max_length=100)
    
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')


        # if password==password2:
        #     user = User(username=username, email=email)
        #     user.set_password(password)
        #     user.save()
        #     return user
        # else:
        #     raise serializers.ValidationError({
        #         'error': 'Both passwords do not match'
        #     })


class UserRegisterSerializer(serializers.ModelSerializer):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User_Details
        exclude = ['date_updated','date_added']
        

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_Details
        exclude = ['date_updated','date_added']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_Booking
        exclude = ['date_updated','date_added']