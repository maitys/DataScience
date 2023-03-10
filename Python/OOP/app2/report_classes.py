import os
import webbrowser
from fpdf import FPDF
 
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
        pdf.image(os.path.join(os.path.dirname(__file__), 'files\house.png'), w=30, h=30)
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
        pdf.output(os.path.join(os.path.dirname(__file__), "files\{}".format(self.filename)))
        #webbrowser.open(os.path.join(os.path.dirname(__file__), "files\{}".format(self.filename))) # open the pdf file in the browser