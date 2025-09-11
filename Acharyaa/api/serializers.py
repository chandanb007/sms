from rest_framework import serializers
from account.models import CustomUser
from core.models import Country

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "email","phone", "groups")
        depth = 1   # expands groups into objects instead of IDs

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("id", "name","iso")
        depth = 1