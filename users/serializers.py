from .models import CustomUser, Payment
from rest_framework.serializers import ModelSerializer


class CustomUserSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'


class PaymentSerializer(ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'
