from rest_framework import routers
from django.urls import path, include
from .views import CustomerViewSet, LoanViewSet, credit_check
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customer')
router.register(r'loans', LoanViewSet, basename='loan')

urlpatterns = [
    path('', include(router.urls)),
    path('credit-check/', credit_check, name='credit-check'),
]
