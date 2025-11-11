from models.loan import Loan
from services.user_service import UserService
from utils.singleton import singleton

@singleton
class LoanService:
    def __init__(self):
        self.loans = {} # {username, [Loans...]}
        self.user_service = UserService()

    def create_loan(self, admin_username, customer_username, principal_amount, loan_tenure, interest_rate, interest_strategy):
        user = self.user_service.get_user(admin_username)

        if user is not None and user.is_user_admin():
            new_loan = Loan(admin_username, customer_username, principal_amount, loan_tenure, interest_rate, interest_strategy)
            if customer_username not in self.loans:
                self.loans[customer_username] = []
            self.loans[customer_username].append(new_loan)
            print("Loan Created Successfully!!!")
        else:
            raise ValueError(f"Admin with username {admin_username} not found!!")

    def make_emi_payments(self, customer_username, amount_paid):
        if customer_username not in self.loans:
            print(f"No loan found for {customer_username}")

        customer_loans = self.loans[customer_username]

        for loan in customer_loans:
            loan.make_emi_payments(amount_paid)

        print(f"Loan paid by {customer_username}")
        

    def fetch_loan_info_by_user(self, customer_username, request_username):
        if customer_username != request_username:
            print("Access Denied")
            return
        
        customer_loans = self.loans[customer_username]
        if customer_loans is not None and len(customer_loans) > 0:
            for loan in customer_loans:
                loan.show_all_info()
        

    def fetch_all_loans(self, admin_username):
        admin = self.user_service.get_user(admin_username)
        if admin is not None and admin.is_user_admin():
            for user_loan in self.loans.values():
                for loan in user_loan:
                    loan.show_all_info()

