from rest_framework import serializers
from .models import User, UserProfile
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer


class CustomUserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'password', 'role', 'nid')


class CustomUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = User
        fields = ('id', 'email', 'role', 'nid')


class UserProfileSerializer(serializers.ModelSerializer):
    profile_picture_url = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'profile_picture_url', 'created_at']
        read_only_fields = ['created_at']

    def get_profile_picture_url(self, obj):
        return obj.profile_picture.url if obj.profile_picture else None
