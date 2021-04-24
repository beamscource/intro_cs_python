
def f(s):
    return 'a' in s

def satisfiesF(L):
    k = []
    for i in L:
        if f(i) == True:
            k.append(i)
    L[:] = k
    return len(L)
