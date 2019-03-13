from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from .models import User
__all__ = (
    'UserCreationSerializer',
    'UserEditionSerializer',
    'UserEditPasswordSerializer',
)


class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('last_login', 'date_joined')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserEditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('last_login', 'date_joined', 'password')


class UserEditPasswordSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'password', 'password_confirm')

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError(_('password does not match'))
        return data

    def update(self, instance, validated_data):
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance
