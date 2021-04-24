
def f(a, b):
    return a + b

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''

    same_keys = []
        
    for key in d1.keys():
        if key in d2.keys():
            same_keys.append(key)

    different_keys = []

    for key in d2.keys():
        if key not in same_keys:
            different_keys.append(key)

    for key in d1.keys():
        if key not in same_keys:
            different_keys.append(key)
    
    dictA = {}
    
    for key in same_keys:
        ans = f(d1[key], d2[key])
        dictA.update({key: ans})

    dictB = {}
    
    for key in different_keys:
        if key in d1.keys():
            ans = d1[key]
            dictB.update({key: ans})
        elif key in d2.keys():
            ans = d2[key]
            dictB.update({key: ans})
    
    result = (dictA, dictB)
    return result

