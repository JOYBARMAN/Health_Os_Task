from rest_framework import serializers
from .models import Customer
from .phone import UniqueNumber

class CustomerRegistrationSerializer(serializers.ModelSerializer):
    unique_phone =UniqueNumber().uniqueNumber()
    phone = serializers.CharField(default=unique_phone)
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = Customer
        fields = ['phone','email','name','password','password2']
        extra_kwargs ={'password':{'write_only':True}}


    def validate(self, attrs):
        password = attrs.get('password')
        password2= attrs.get('password2')
        if len(password)<8:
            raise serializers.ValidationError("Password less than 8 character")
        if password != password2:
            raise serializers.ValidationError("Password don't match")
        return attrs

    def create(self, validated_data):
        return Customer.objects.create_user(**validated_data)


class CustomerLoginSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=100)
    class Meta:
        model = Customer
        fields = ['phone','password']