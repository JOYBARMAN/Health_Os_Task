from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import GetPhoneNumberSerializer,PostPhoneNumberSerializer
from .models import PhoneNumbers
from customer_accounts_api.renderer import CustomerRenderers
from rest_framework import status

class PhoneNumberView(APIView):
    renderer_classes = [CustomerRenderers]
    def get(self,request,format=None):
        phoneNum = PhoneNumbers.objects.all()
        serializer = GetPhoneNumberSerializer(phoneNum,many=True)
        return Response({"msg":"Successful","data":serializer.data},status=status.HTTP_200_OK)

    def post(self,request,format=None):
        serializer = PostPhoneNumberSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg":"Successfully add phone number"},status=status.HTTP_201_CREATED)