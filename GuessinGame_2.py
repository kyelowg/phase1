#Kye Lowmon 
#CIS261
#Phase One Lab
def GetEmpName():
    empname = input("Enter employee name: ")
    return empname

def GetHoursWorked():
    hours = int(input('Enter employee hours: '))
    return hours

def GetHourlyRate():
    hourlyrate = int(input("Enter employee's hourly rate: "))
    return hourlyrate

def GetTaxRate():
    taxrate = int(input("Enter employee's tax rate: "))
    return taxrate/100
    print()


def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay


def printinfo(empname, hours, hourlyrate,grosspay, taxrate, incometax, netpay):
    print(empname, f"{hours:,.2f}",  f"{hourlyrate:,.2f}", f"{grosspay:,.2f}",  f"{taxrate:.0%}",  f"{incometax:,.2f}",  f"{netpay:,.2f}")

def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):    
    print()
    print(f"Total Number Of Employees: {TotEmployees}")
    print(f"Total Employee Hours: {TotHours:,.2f} ")
    print(f'Total Gross Pay Amount: {TotGrossPay:,.2f} ')
    print(f'Total Amount Of Taxes: {TotTax:.0%} ')
    print(f'Total Net Pay Amount: {TotNetPay:,.2f} ')


if __name__ == "__main__":
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        hours = GetHoursWorked()
            
        hourlyrate = GetHourlyRate()
        taxrate = GetTaxRate()


      

            


        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay)
       
        TotEmployees += 1
        TotHours += 1
        TotGrossPay += 1.00
        TotTax += 1
        TotNetPay += 1.00
        


    PrintTotals (TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay)


