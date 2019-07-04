from rest_framework import serializers
from api.models import User
from django.contrib.auth import password_validation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email', 'last_name', 'first_name', 'phone', 'password'
        )
        extra_kwargs = {'password': {'write_only': True} }
        write_only_fields = ('password', 'email')

    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        return value


    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email', 'last_name', 'first_name', 'phone',
        )
        extra_kwargs = {'email': {'read_only': True} }
