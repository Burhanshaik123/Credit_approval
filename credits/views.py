from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .models import Customer, Loan
from .serializers import CustomerSerializer, LoanSerializer
from django.shortcuts import get_object_or_404

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

@api_view(['POST'])
def credit_check(request):
    """Simple credit decision API:
       Expects: customer_id, requested_amount
    """
    data = request.data
    cid = data.get('customer_id')
    amount = float(data.get('requested_amount', 0))
    if cid is None:
        return Response({'approved': False, 'reason': 'customer_id required'}, status=400)
    try:
        customer = Customer.objects.get(customer_id=cid)
    except Customer.DoesNotExist:
        return Response({'approved': False, 'reason': 'customer not found'}, status=404)
    # Simple decision rules:
    # - If requested amount <= approved_limit: approve
    # - Else if monthly_salary * 12 * 5 >= amount: approve (DTI rule)
    # - Else reject
    if amount <= customer.approved_limit:
        return Response({'approved': True, 'reason': 'within approved limit'})
    if customer.monthly_salary * 12 * 5 >= amount:
        return Response({'approved': True, 'reason': 'income supports loan (5x annual salary)'})
    return Response({'approved': False, 'reason': 'insufficient income or limit'})
