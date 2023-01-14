from rest_framework import serializers
from .models import SubscriptionPlan , Subscription

class GetSubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = ('id','name','company','fee','duration','description')
        depth = 1

class PostSubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = ('name','company','fee','duration','description')

class GetSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('id','customer','phone_number','plan','start_date','end_date','cancel_subscripton','is_pay')
        depth = 1

class PostSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('customer','phone_number','plan')
