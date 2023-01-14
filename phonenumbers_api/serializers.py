from rest_framework import serializers
from .models import PhoneNumbers

class GetPhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumbers
        fields = ('id','customer','company','phone_number')
        depth = 1

class PostPhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumbers
        fields = ('customer','company','phone_number')