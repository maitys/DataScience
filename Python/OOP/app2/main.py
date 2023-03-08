import os
import webbrowser
from fpdf import FPDF


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
    
############################################
#### Class: PdfReport ####
############################################
class PdfReport:
    """
    Create a PDF report of the bill with the period, name of the flatmate and amount of money each flatmate has to pay
    """
    def __init__(self, filename):
        self.filename = filename
        
    def generate(self, flatmate1, flatmate2, total_bill):
        
        pdf = FPDF(orientation='P', unit='pt', format='A4') # initilize the pdf object
        pdf.add_page() # add a page
        
        # Add iccon to the pdf
        pdf.image(os.path.join(os.path.dirname(__file__), 'house.png'), w=30, h=30)
        
        pdf.set_font(family='Times', style='B', size=24)

        # Add a title
        pdf.cell(w=0, h=60, txt='Flatmates Bill', border=1, align="C", ln=1) # ln=1 means new line

        # Add the period and value
        pdf.set_font(family='Arial', style='B', size=12)
        pdf.set_text_color(0, 0, 0) # black
        pdf.cell(w=50, h=25, txt='Period', border=1, align="L", ln=0)
        pdf.cell(w=100, h=25, txt=total_bill.period, border=1, align="L", ln=1)
        
        # Add the name and amount for flatmate 1
        pdf.set_font(family='Times', style='I', size=12)
        pdf.set_text_color(255, 0, 0) # red
        flatmate1_pay = str(round(flatmate1.pays(total_bill, flatmate2),1))
        pdf.cell(w=50, h=25, txt=flatmate1.name, border=1, align="L", ln=0)
        pdf.cell(w=100, h=25, txt="$ " + flatmate1_pay , border=1, align="L", ln=1)
        
        # Add the name and amount for flatmate 2
        pdf.set_font(family='Times', style='I', size=12)
        pdf.set_text_color(255, 0, 0) # red
        flatmate2_pay = str(round(flatmate2.pays(total_bill, flatmate1),1))
        pdf.cell(w=50, h=25, txt=flatmate2.name, border=1, align="L", ln=0)
        pdf.cell(w=100, h=25, txt="$ " + flatmate2_pay, border=1, align="L", ln=1)

        # save pdf in the same directory as this file
        pdf.output(os.path.join(os.path.dirname(__file__), self.filename))
        # webbrowser.open(os.path.join(os.path.dirname(__file__), self.filename)) # open the pdf file in the browser


#######################################################
##### Below is the code to test the above classes #####
#######################################################
march_bill = Bill(amount=120, period="March 2021")
print(march_bill.amount)
john = Flatmate(name="John", days_in_house=20)
marry = Flatmate(name="Marry", days_in_house=25)
print(john.name)
print(marry.name)
print(john.pays(march_bill, other_flatmate=marry))
print(marry.pays(march_bill, other_flatmate=john))
pdf_report = PdfReport(filename="flatmates_bill.pdf")
pdf_report.generate(flatmate1=john, flatmate2=marry, total_bill=march_bill)