"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from customer_accounts_api.views import CustomerRegistrationView,CustomerLoginView
from company_api.views import CompanyView
from phonenumbers_api.views import PhoneNumberView
from subscription_api.views import SubscriptionPlanView,CustomerSubscriptionView,CustomerAddSubscription,CustomerCancelSubView
from payment_api.views import CustomerPaymentSubscription

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/reg/',CustomerRegistrationView.as_view()),
    path('api/login/',CustomerLoginView.as_view()),
    path('api/company/',CompanyView.as_view()),
    path('api/phonenum/',PhoneNumberView.as_view()),
    path('api/subplan/',SubscriptionPlanView.as_view()),
    path('api/addsub/',CustomerAddSubscription.as_view()),
    path('api/cussub/<int:uid>/',CustomerSubscriptionView.as_view()),
    path('api/payment/<int:subid>/',CustomerPaymentSubscription.as_view()),
    path('api/cancelsub/<int:subid>/',CustomerCancelSubView.as_view())
]
