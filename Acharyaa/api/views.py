from rest_framework import generics, permissions
from account.models import CustomUser
from core.models import Country
from .serializers import UserSerializer, CountrySerializer
from rest_framework.permissions import DjangoModelPermissions

# List + Create users
class UserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [DjangoModelPermissions]

# Retrieve, Update, Delete single user
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class CountriesListView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    