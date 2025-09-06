from rest_framework import serializers
from account.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "email", "role", "phone", "groups")
        depth = 1   # expands groups into objects instead of IDs
