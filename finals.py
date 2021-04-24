
def f(n):
    def g(m):
        m = 0
        for i in range(m):
            print m
    for i in range(n):
        g(n)


def dict_invert(d):
    inv = {}
    for k, v in d.iteritems():
        keys = inv.setdefault(v, [])
        keys.append(k)
        keys.sort()
    return inv

def getSublists(L, n):

    finalList = []

    for e in range(len(L)):
        if e < len(L)-(n-1):
            sublist = L[e:e+n]
            finalList.append(sublist)

    return finalList 
    
def longestRun(L):

    longest = []
    answer = 0

    for i in range(len(L)):
        longest = []
        longest.append(L[i])
        e = i
        
        try:
            while longest[-1] <= L[e+1]:
                longest.append(L[e+1])
                e += 1
                if len(longest) > answer:
                    answer = len(longest)
        except IndexError:
            continue

    if len(longest) > answer:
                    answer = len(longest)

    return answer
