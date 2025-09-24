# Backend Internship Assignment - Credit Approval System (Minimal Implementation)

This is a minimal Django + DRF implementation to complete the backend assignment:
- Models: Customer, Loan
- API endpoints: /api/customers/, /api/loans/, /api/credit-check/ (POST: customer_id, requested_amount)
- Management command `import_seed` to import provided Excel files (place them in `./data/` folder)
- Dockerized with docker-compose; the compose command runs migrations and imports seed data.

How to run locally:
1. Copy `customer_data.xlsx` and `loan_data.xlsx` into the `data` folder (already provided).
2. Build and run:
   ```bash
   docker-compose up --build
   ```
3. API will be available at http://localhost:8000/api/

Notes:
- This is a minimal, clear, and extensible starting point. Decision rules in `credit-check` are simple and can be extended.
