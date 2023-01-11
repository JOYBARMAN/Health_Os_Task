from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CompanySerializer
from .models import Company
from customer_accounts_api.renderer import CustomerRenderers
from rest_framework import status

class CompanyView(APIView):
    renderer_classes = [CustomerRenderers]
    def get(self,request,format=None):
        company = Company.objects.all()
        serializer = CompanySerializer(company,many=True)
        return Response({"msg":"Successful","data":serializer.data},status=status.HTTP_200_OK)

    def post(self,request,format=None):
        serializer = CompanySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg":"Successfully add data"},status=status.HTTP_201_CREATED)