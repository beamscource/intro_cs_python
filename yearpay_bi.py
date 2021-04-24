'''
Second problem set, third problem
'''

balance = 4142
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate/12.0
lowerBound = balance/12
upperBound = (balance + (balance*annualInterestRate))/12
initBalance = balance
endBalance = 1

while endBalance > 0 or endBalance < -1:

    lowestPayment = (upperBound + lowerBound)/2
   
    for m in range(1, 13):

        unpaidBalance = initBalance - lowestPayment         
        initBalance = unpaidBalance + unpaidBalance * monthlyInterestRate

        print 'Month: ' + str(m)
        print 'Minimum monthly payment: ' + str(round(lowestPayment, 2))
        print 'Remaining balance: ' + str(round(initBalance, 2))
    
    endBalance = initBalance

    if endBalance > 0:
        lowerBound = lowestPayment
    elif endBalance < -1:
        upperBound = lowestPayment
            
            
    initBalance = balance

print 'Lowest Payment: ' + str(round(lowestPayment, 2))
