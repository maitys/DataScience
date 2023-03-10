############################################
#### Class: Bill ####
############################################
class Bill:
    """
    Object that represents a single bill amount and period of the bill
    amount: float
    period: str
    """
    
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

############################################
#### Class: Flatmate ####
############################################
class Flatmate:
    """
    Object that represents a single flatmate person and pays a share of the bill
    name: str
    days_in_house: int
    """
    
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, total_bill, other_flatmate):
        weight = self.days_in_house / (self.days_in_house + other_flatmate.days_in_house)
        to_pay =  round(total_bill.amount * weight, 2)
        return to_pay