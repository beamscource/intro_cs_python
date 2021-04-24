

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

class USResident(Person):
    """ 
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        Person.__init__(self, name)
        if status != 'citizen' and status != 'legal_resident' and status != 'illegal_resident':
            raise ValueError
        else:
            self.status = status
        
    def getStatus(self):
        """
        Returns the status
        """
        return self.status

