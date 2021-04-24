
target = 'bob'
targetCount = 0
l = len(s) - 2
n = 0
while l != 0:
    if target in s[n:n+3]:
       targetCount = targetCount + 1
    l -= 1
    n += 1
print 'Number of times bob occurs is: ' + str(targetCount)
