from django.core.management.base import BaseCommand
import pandas as pd
from django.conf import settings
from credits.models import Customer, Loan
from pathlib import Path
class Command(BaseCommand):
    help = 'Import seed data from customer_data.xlsx and loan_data.xlsx placed in /data'

    def handle(self, *args, **options):
        data_dir = Path('/data')
        cust_file = data_dir / 'customer_data.xlsx'
        loan_file = data_dir / 'loan_data.xlsx'
        if cust_file.exists():
            df = pd.read_excel(cust_file)
            for _, row in df.iterrows():
                Customer.objects.update_or_create(
                    customer_id = int(row.get('Customer ID')),
                    defaults = dict(
                        first_name = row.get('First Name') or '',
                        last_name = row.get('Last Name') or '',
                        age = int(row.get('Age')) if not pd.isna(row.get('Age')) else None,
                        phone_number = str(row.get('Phone Number') or ''),
                        monthly_salary = float(row.get('Monthly Salary') or 0),
                        approved_limit = float(row.get('Approved Limit') or 0),
                    )
                )
            self.stdout.write('Customers imported.')
        else:
            self.stdout.write('customer_data.xlsx not found in /data')

        if loan_file.exists():
            df = pd.read_excel(loan_file)
            for _, row in df.iterrows():
                cid = int(row.get('Customer ID'))
                try:
                    customer = Customer.objects.get(customer_id=cid)
                except Customer.DoesNotExist:
                    continue
                Loan.objects.update_or_create(
                    loan_id = int(row.get('Loan ID')),
                    customer = customer,
                    defaults = dict(
                        loan_amount = float(row.get('Loan Amount') or 0),
                        tenure = int(row.get('Tenure') or 0),
                        emIs_paid_on_time = int(row.get('... EMIs paid on Time') or 0) if not pd.isna(row.get('... EMIs paid on Time')) else None,
                        date_of_approval = row.get('Date of Approval') if not pd.isna(row.get('Date of Approval')) else None,
                        end_date = row.get('End Date') if not pd.isna(row.get('End Date')) else None,
                    )
                )
            self.stdout.write('Loans imported.')
        else:
            self.stdout.write('loan_data.xlsx not found in /data')
