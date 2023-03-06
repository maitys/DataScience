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

    def pays(self, total_bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay =  round(total_bill.amount * weight, 2)
        return to_pay
    
############################################
#### Class: PdfReport ####
############################################
class PdfReport:
    """
    Create a PDF report of the bill with the period, name of the flatmate and amount of money each flatmate has to pay
    """
    
    def generate(self, flatmate1, flatmate2, bill):
        pass
    



# Below is the code to test the above classes
march_bill = Bill(amount=120, period="March 2021")
john = Flatmate(name="John", days_in_house=20)
marry = Flatmate(name="Marry", days_in_house=25)
print(march_bill.amount)
print(john.name)
print(marry.name)
print(john.pays(march_bill, flatmate2=marry))
print(marry.pays(march_bill, flatmate2=john))