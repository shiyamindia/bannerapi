"""
Serializers for user api view
"""

from django.contrib.auth import (
    get_user_model,
    authenticate,
)

from django.utils.translation import gettext as T
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """ Serializers for the user object """

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password':{'write_only': True, 'min_length' : 5}}

    def create(self, validated_data):
        """ Create and return a user with encrypted data """
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update and return user."""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user

class AuthTokenSerializer(serializers.Serializer):
    """ Serializer for auth token """

    email = serializers.EmailField()
    password = serializers.CharField(
        style ={'input_type':'password'},
        trim_whitespace = False,
    )

    def Validate(self, attrs):
        """ Validation for authenticate the user """
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password = password,
        )
        if not user:
            msg = T('Unable to authenticate with given credentials')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs



