from rest_framework import serializers
from api.models import Company

class UserSerializer(serializers.ModelSerializer):
    """Serializes the User data"""
    class Meta:
        model = Company
        fields = (
            'company_name', 'industry_type', 'phone', 'address', 'added_by', 'added_date'
        )

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
