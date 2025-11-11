class Loan:
    def __init__(self, admin_username, customer_username, principal_amount, loan_tenure, interest_rate, interest_strategy):
        self.admin_username = admin_username
        self.customer_username = customer_username
        self.principal_amount = principal_amount
        self.loan_tenure = loan_tenure
        self.interest_rate = interest_rate
        self.remaining_principal = principal_amount
        self.emi_payments = []
        self.calculate_emi_payments(interest_strategy)

    def calculate_emi_payments(self, interest_strategty):
        interest_value = interest_strategty.calculate_interest(self.principal_amount, self.interest_rate, self.loan_tenure)
        total_amount = self.principal_amount + interest_value

        emi = total_amount // (self.loan_tenure*12)
        for _ in range(0, self.loan_tenure*12):
            self.emi_payments.append(emi)

        self.remaining_principal = total_amount

    def make_emi_payments(self, amount_paid):
        if self.remaining_principal > 0 and len(self.emi_payments) > 0:
            self.remaining_principal -= amount_paid
            self.emi_payments.pop(0)

    def show_all_info(self):
        print(f"INFO ABOUT LOAN FOR {self.customer_username}")
        print("Admin: ", self.admin_username)
        print("Customer: ", self.customer_username)
        print(f"Principal: {self.principal_amount}, Loan Tenure: {self.loan_tenure}, Rate: {self.interest_rate}")
        print("Remaining Principle: ", self.remaining_principal)
        print("EMI Payments done: ", self.loan_tenure*12 - len(self.emi_payments))
        print("Remaining EMIs: ", len(self.emi_payments))

    def get_customer_name(self):
        return self.customer_username