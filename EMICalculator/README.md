https://www.anucodes.in/blog/Interview-Experience-for-Senior-Software-Engineer-at-Razorpay-Machine-Coding-Round


Entities

User - (username, is_admin) => both of these have get and set funcs.
Loan - (admin_username, customer_username, principal_amount, loan_tenure, interest_rate, emi_payments: [], remaining_principal)
    - calculate_emi_payments()
    - make_emi_payments()
    - show_all_info_about_loan
    - customer_name()
UserService - create_user(), get_user() - Make singleton
LoanService - create_loan(), make_emi_payments(), fetch_loan_info(), fetch_all_loans() - Make singleton

InterestStrategy
    - Strategy Pattern
    - SimpleInterestStrategy

