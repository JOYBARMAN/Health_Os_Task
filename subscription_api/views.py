from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import GetSubscriptionPlanSerializer,PostSubscriptionPlanSerializer,GetSubscriptionSerializer,PostSubscriptionSerializer
from .models import SubscriptionPlan,Subscription
from customer_accounts_api.renderer import CustomerRenderers
from rest_framework import status

class SubscriptionPlanView(APIView):
    renderer_classes = [CustomerRenderers]
    def get(self,request,format=None):
        subPlan = SubscriptionPlan.objects.all()
        serializer = GetSubscriptionPlanSerializer(subPlan,many=True)
        return Response({"msg":"Successful","data":serializer.data},status=status.HTTP_200_OK)

    def post(self,request,format=None):
        serializer = PostSubscriptionPlanSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg":"Successfully add data"},status=status.HTTP_201_CREATED)


class CustomerAddSubscription(APIView):
    renderer_classes = [CustomerRenderers]
    def post(self,request,format=None):
        serializer = PostSubscriptionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg":"Successfully Subscribe"},status=status.HTTP_201_CREATED)


class CustomerSubscriptionView(APIView):
    renderer_classes = [CustomerRenderers]
    def get(self,request,uid,format=None):
        # user = request.user
        print(request.user)
        customerSub = Subscription.objects.filter(customer=uid)
        serializer = GetSubscriptionSerializer(customerSub,many=True)
        return Response({"msg":"Successful","data":serializer.data},status=status.HTTP_200_OK)


class CustomerCancelSubView(APIView):
    renderer_classes = [CustomerRenderers]
    def post(self,request,subid,format=None):
        try:
            subscription = Subscription.objects.get(id=subid)
            cusSubs = Subscription.objects.filter(customer=subscription.customer)
            if len(cusSubs)>1:
                subscription.cancel_subscripton = True
                subscription.save()
                return Response({"msg":"Your Subscribtion Canceled"},status=status.HTTP_201_CREATED)
            else:
                return Response({"msg":"You must have at least one subscription"})
        except:
            return Response({"errors":"Does not exits"})