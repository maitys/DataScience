import os
from flat_classes import Bill, Flatmate
from report_classes import PdfReport, FileSharer


print("*** Welcome to the Flatmates Bill Calculator ***")
amount = float(input("Hey user, enter the bill amount: "))
period = input("What is the bill period? E.g. January 2021: ")
name_flatmate1 = input("What is the name of the 1st flatmate? ")
days_in_house1 = int(input("How many days has the 1st flatmate stayed in the house during the bill period? "))
name_flatmate2 = input("What is the name of the 2nd flatmate? ")
days_in_house2 = int(input("How many days has the 2nd flatmate stayed in the house during the bill period? "))

print("\n*** Data entered ***")
print("Total bill: $", amount, " for ", period)
print("Flatmate 1: ", name_flatmate1, " stayed ", days_in_house1, " days")
print("Flatmate 2: ", name_flatmate2, " stayed ", days_in_house2, " days")

print("\n*** Calculating the bill...***")
month_bill = Bill(amount=amount, period=period)
flatmate1 = Flatmate(name=name_flatmate1, days_in_house=days_in_house1)
flatmate2 = Flatmate(name=name_flatmate2, days_in_house=days_in_house2)
flatmate1_pays = flatmate1.pays(month_bill, other_flatmate=flatmate2)
flatmate2_pays = flatmate2.pays(month_bill, other_flatmate=flatmate1)
print(flatmate1.name, " pays: $", flatmate1_pays)
print(flatmate2.name, " pays: $", flatmate2_pays)

pdf_report = PdfReport(filename="{period}.pdf".format(period=month_bill.period))
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, total_bill=month_bill)

file_sharer = FileSharer(filepath= os.path.join(os.path.dirname(__file__), "files\{}".format(pdf_report.filename)))
print(file_sharer.share())