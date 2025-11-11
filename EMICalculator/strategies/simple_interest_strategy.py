from strategies.interest_strategy import InterestStrategy

class SimpleInterestStrategy(InterestStrategy):
    def calculate_interest(self, principal, rate, tenure):
        return (principal * rate * tenure) // 100