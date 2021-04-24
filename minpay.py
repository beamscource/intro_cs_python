'''
Second problem set, first problem
'''

balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate/12.0
totalPaid = 0
initBalance = balance

for m in range(1, 13):

    
    minMonthlyPayment = initBalance * monthlyPaymentRate
    unpaidBalance = initBalance - minMonthlyPayment
    
    initBalance = unpaidBalance + unpaidBalance * monthlyInterestRate

    totalPaid = totalPaid + minMonthlyPayment  

    print 'Month: ' + str(m)
    print 'Minimum monthly payment: ' + str(round(minMonthlyPayment, 2))
    print 'Remaining balance: ' + str(round(initBalance, 2))

print 'Total paid: ' + str(round(totalPaid, 2))
print 'Remaining balance: ' + str(round(initBalance, 2))
