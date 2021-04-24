
s = 'aaaaaaaaasdf'
vowels = 'aeiou'
vowelCount = 0
l = len(s)
n = 0
while l != 0:
    print (s[n])
    if vowels.find(s[n]) != -1:
       print (vowels.find(s[n]))
       vowelCount = vowelCount + 1
    l -= 1
    n += 1
print 'Number of vowels: ' + str(vowelCount)
