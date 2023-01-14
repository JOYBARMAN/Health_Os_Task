from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PaymentSerializer
from subscription_api.models import Subscription,SubscriptionPlan
from customer_accounts_api.renderer import CustomerRenderers
from rest_framework import status
from customer_accounts_api.models import Customer
from datetime import date,timedelta

# find the date of given day
def find_date(year, current_day):
    days_in_year = 365
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_year = 366
    return date(year, 1, 1) + timedelta(days=current_day-1)



class CustomerPaymentSubscription(APIView):
    renderer_classes = [CustomerRenderers]
    def post(self,request,subid,format=None):
        today = date.today()
        expair_date = today.day+30
        year = today.year
        if expair_date>365:
            new_date=expair_date-365
            new_year = year+1
            expair_date = new_date
            year=new_year
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            subscription=Subscription.objects.get(id=subid)
            subscription.is_pay = True
            subscription.start_date=today
            subscriptionPlan=SubscriptionPlan.objects.get(id=subscription.plan.id)
            if subscriptionPlan.duration == "Yearly":
                year=year+1
                day=today.day
                subscription.end_date = find_date(year,day)
            else:
                subscription.end_date = find_date(year,expair_date)
            subscription.save()
            serializer.save()
            return Response({"msg":"Payment Sucessfully Done"},status=status.HTTP_201_CREATED)

