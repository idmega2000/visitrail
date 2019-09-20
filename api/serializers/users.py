from rest_framework import serializers
from api.models import User, CompanyUser, Company
from django.contrib.auth import password_validation
from api.helpers.random_string_gen import random_string_gen
from rest_framework.fields import CurrentUserDefault

class UserSerializer(serializers.ModelSerializer):
    """Serializes the User data"""
    class Meta:
        model = User
        fields = (
            'email', 'last_name', 'first_name', 'phone', 'password'
        )
        extra_kwargs = {'password': {'write_only': True} }

    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        return value

    def create(self, validated_data):
        """creates the user
        Args:
            validated_data(dict): data that has been validated
        """

        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class UpdateUserSerializer(serializers.ModelSerializer):
    """Handles user data update """
    class Meta:
        model = User
        fields = (
            'email', 'last_name', 'first_name', 'phone',
        )
        extra_kwargs = {'email': {'read_only': True} }


class CompanyUserSerializer(serializers.ModelSerializer):

    """Handles company user data """
    class Meta:
        model = CompanyUser
        fields = (
            'email', 'last_name', 'first_name', 'phone', 'password', 'image_url', 'added_by', 'company'
        )

    def validate(self, data):
        print(data)
        norm_email = data['email'].lower()
        company = data['company']
        if CompanyUser.objects.filter(email=norm_email, company=company).exists():
            raise serializers.ValidationError(f"{norm_email} already exist")
        data['image_url'] = 'game'
        return data
        

    def create(self, validated_data):
        """creates the company user
        Params:
            validated_data(dict): data that has been validated
        Returns:
            the instance of the Companyuser
        """

        instance = self.Meta.model(**validated_data)
        instance.password = random_string_gen(15)
        instance.save()
        return instance


