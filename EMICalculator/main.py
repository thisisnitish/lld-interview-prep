from services.user_service import UserService
from services.loan_service import LoanService
from strategies.simple_interest_strategy import SimpleInterestStrategy


def run():

    user_service = UserService()
    user_service.create_user("Nitish", True)
    user_service.create_user("Prashant", False)

    loan_service = LoanService()
    loan_service.create_loan("Nitish", "Prashant", 10000, 2, 5, SimpleInterestStrategy())

    loan_service.fetch_all_loans("Nitish")
    print("=================================")
    loan_service.fetch_loan_info_by_user("Prashant", "Prashant")
    print("=================================")
    loan_service.make_emi_payments("Prashant", 1500)
    print("=================================")

    loan_service.fetch_all_loans("Nitish")

if __name__ == "__main__":
    run()