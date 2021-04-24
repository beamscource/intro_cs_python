## ProblemSet 1

# get number of vowels in a string

vowels = 'aeiou'
vowelCount = 0
l = len(s)
n = 0
while l != 0:
    if vowels.find(s[n]) != -1:
       vowelCount = vowelCount + 1
    l -= 1
    n += 1
print 'Number of vowels: ' + str(vowelCount)

# counting bobs (boobs)

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

# counting and grouping

def item_order(order):
    '''
    item_order takes as input a string, which is a list of items,
    breaks them up, counts them and group them
    '''

    targetS = 'salad'
    targetH = 'hamburger'
    targetW = 'water'

    countS = 0
    countH = 0
    countW = 0

    for n in range(len(order)+1):

        try:
            if targetS in order[n:n+len(targetS)]:
                countS += 1
        
            elif targetH in order[n:n+len(targetH)]:
                countH += 1

            elif targetW in order[n:n+len(targetW)]:
                countW += 1
        except IndexError:
            return

    return ('salad:' + str(countS) + ' hamburger:' + str(countH) + ' water:' + str(countW))
