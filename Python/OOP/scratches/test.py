from fpdf import FPDF
import os
pdf = FPDF(orientation='P', unit='pt', format='A4') # initilize the pdf object
pdf.add_page() # add a page
pdf.set_font(family='Times', style='B', size=24)

# Add a title
pdf.cell(w=100, h=80, txt='Flatmates Bill', border=1, align="C", ln=1) # ln=1 means new line
pdf.cell(w=50, h=40, txt='Period', border=1, align="L", ln=1)
pdf.cell(w=50, h=40, txt='March 2021', border=1, align="L", ln=1)
pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align="C", ln=1) # ln=1 means new line
# on a new line, add text hello world with font size 10
pdf.set_font(family='Times', style='B', size=10)
pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align="C", ln=1) # ln=1 means new line

# save pdf in the same directory as this file
pdf.output(os.path.join(os.path.dirname(__file__), 'flatmates_bill.pdf'))