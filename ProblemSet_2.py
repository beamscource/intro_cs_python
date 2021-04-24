## ProblemSet 2

# paying minimum credit card funds

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

# paying debt in a year

monthlyInterestRate = annualInterestRate/12.0
factor = 10
lowestPayment = 0
initBalance = balance
endBalance = 1

while endBalance > 0:
   
    for m in range(1, 13):

        unpaidBalance = initBalance - lowestPayment         
        initBalance = unpaidBalance + unpaidBalance * monthlyInterestRate

    endBalance = initBalance
    initBalance = balance
    lowestPayment = lowestPayment + factor

print 'Lowest Payment: ' + str(round(lowestPayment-10, 2))

# last problem usind bisection serch algorithm

monthlyInterestRate = annualInterestRate/12.0
factor = 10
lowestPayment = 0
initBalance = balance
endBalance = 1

while endBalance > 0:
   
    for m in range(1, 13):

        unpaidBalance = initBalance - lowestPayment         
        initBalance = unpaidBalance + unpaidBalance * monthlyInterestRate

    endBalance = initBalance
    initBalance = balance
    lowestPayment = lowestPayment + factor

print 'Lowest Payment: ' + str(round(lowestPayment-10, 2))


