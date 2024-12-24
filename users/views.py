from rest_framework import viewsets
from .serializers import CustomUserSerializer, PaymentSerializer
from .models import CustomUser, Payment
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class CustomUserViewSet(viewsets.ModelViewSet):

     model = CustomUser
     serializer_class = CustomUserSerializer
     queryset = CustomUser.objects.all()


class PaymentViewSet(viewsets.ModelViewSet):

     model = Payment
     serializer_class = PaymentSerializer
     queryset = Payment.objects.all()
     filter_backends = [DjangoFilterBackend, OrderingFilter]
     filterset_fields = ['course', 'lesson', 'method']
     orderind_fields = ['payment_date']