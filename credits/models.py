from django.db import models
class Customer(models.Model):
    customer_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    monthly_salary = models.FloatField(default=0)
    approved_limit = models.FloatField(default=0)

    def __str__(self):
        return f"{self.customer_id} - {self.first_name} {self.last_name}"

class Loan(models.Model):
    customer = models.ForeignKey(Customer, related_name='loans', on_delete=models.CASCADE)
    loan_id = models.IntegerField()
    loan_amount = models.FloatField()
    tenure = models.IntegerField(help_text='in months')
    emIs_paid_on_time = models.IntegerField(null=True, blank=True)
    date_of_approval = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    monthly_installment = models.FloatField(null=True, blank=True)
    repayments_left = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Loan {self.loan_id} for Customer {self.customer.customer_id}"
