# Monthly Interest Rate Calculation Example #

import calendar

# 47,000 @ 6% annual rate

loan = 47000

# base interest rate on current RPI in UK 
a_int_rate = 6/100 # annual interest rate
m_int_rate = a_int_rate/12

# monthly repayment at start (month 0)
x = loan * m_int_rate

print("\nmonthly payment = " + str(x))
print("\nmonthly rate " + str(m_int_rate),"\n")

# Repay £11 per month for year 1 : what is the oustanding balance at end of the year?
repayment = 11

for i in range (2,13):

    month_name = (calendar.month_name[i])

    loan = loan + (loan * m_int_rate) # interest added on for the month
    loan = loan - repayment # ( updated balance minus the £11 payment)
    print(f"Balance on 1st of month {month_name:<10}","\t\t\t", str(round(loan,2)) )
