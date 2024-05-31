# serializers.py
from rest_framework import serializers
from .models import CustomUser, Staff, Attendance


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'is_staff', 'is_manager']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


# serializers.py
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['user', 'working_days', 'shifts']


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['staff', 'image']
        # Add 'image' field as an ImageField
        extra_kwargs = {'image': {'required': True, 'allow_empty_file': False}}
