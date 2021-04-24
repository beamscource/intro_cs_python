

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''

    pairProduct = []
    for i in range(len(listA)):
        for j in range(len(listB)):
            if j == i:
                pairProduct.append(listA[i]*listB[j])

    return sum(pairProduct)
