from django.urls import path
from . import views


urlpatterns = [
    path('', views.checkout, name="checkout" ),
    path('checkout_succeed/<order_code>', views.checkout_succeed, name='checkout_succeed'),
    
  
]