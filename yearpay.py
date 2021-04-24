'''
Second problem set, second problem
'''

balance = 999999
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate/12.0
factor = 0.001
lowestPayment = 100
initBalance = balance
endBalance = 1

while endBalance > 0:
   
    for m in range(1, 13):

        unpaidBalance = initBalance - lowestPayment         
        initBalance = unpaidBalance + unpaidBalance * monthlyInterestRate

        #print 'Month: ' + str(m)
        #print 'Minimum monthly payment: ' + str(round(lowestPayment, 2))
        print 'Remaining balance: ' + str(round(initBalance, 2))

    endBalance = initBalance
    initBalance = balance
    lowestPayment = lowestPayment + factor

print 'Lowest Payment: ' + str(round(lowestPayment-10, 2))

# ((balance/1000)*100) - 200 # finding the start min payment
