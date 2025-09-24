from rest_framework import serializers
from .models import Customer, Loan

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    loans = LoanSerializer(many=True, read_only=True)
    class Meta:
        model = Customer
        fields = '__all__'
