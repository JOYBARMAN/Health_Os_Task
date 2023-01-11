from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import CustomerRegistrationSerializer,CustomerLoginSerializer
from .renderer import CustomerRenderers
from django.contrib.auth import authenticate

# cutomer registration view 
class CustomerRegistrationView(APIView):
    renderer_classes = [CustomerRenderers]
    def post(self,request,format=None):
        serializer = CustomerRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # token = get_tokens_for_user(user)
        return Response({"msg":"Registration Sucessful","Your unique phone number is":serializer.data['phone']},status=status.HTTP_201_CREATED)

# cutomer Login view 
class CustomerLoginView(APIView):
    renderer_classes = [CustomerRenderers]
    def post(self,request,format=None):
        serializer = CustomerLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone=serializer.data.get("phone")
        password=serializer.data.get("password")
        customer=authenticate(phone=phone,password=password)
        if customer is not None:
            # token = get_tokens_for_user(user)
            return Response({"msg":"Login Sucessful"},status=status.HTTP_200_OK)
        else:
            return Response({"errors":{"non_field_errors":"Phone or Password is not valid"}},status=status.HTTP_404_NOT_FOUND)  