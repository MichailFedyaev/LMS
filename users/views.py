from rest_framework import viewsets
from .serializers import CustomUserSerializer
from .models import CustomUser


class CustomUserViewSet(viewsets.ModelViewSet):

     model = CustomUser
     serializer_class = CustomUserSerializer
     queryset = CustomUser.objects.all()