## finger er

# Week 1 + week 2

print('hello world')

if happy > 2:
    print('hello world')

x = 2
while x < 11:
    print x
    x += 2
print 'Goodbye!

for n in range(2, 12, 2):
   print n
print 'Goodbye!'

iteration = 0
count = 0
while iteration < 5:
    # the variable 'letter' in the loop stands for every 
    # character, including spaces and commas!
    for letter in "hello, world": 
        count += 1
    print "Iteration " + str(iteration) + "; count is: " + str(count)
    iteration += 1

iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
    print "Iteration " + str(iteration) + "; count is: " + str(count)
    iteration += 1

x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) < epsilon:
        break
    else:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print 'failed'
else:
    print 'succeeded: ' + str(guess)

x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) >= epsilon:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print 'failed'
else:
    print 'succeeded: ' + str(guess)

## secret number guessing game #####

print 'Please think of a number between 0 and 100!'
lowerEnd = 0
higherEnd = 100
boundary = 'l'

while boundary != 'c':
    guess = (higherEnd + lowerEnd)/2 
    print 'Is your secret number ' + str(guess) + '?'
    boundary = raw_input('Enter ''h'' to indicate the guess is too high. \
    Enter ''l'' to indicate the guess is too low. \
    Enter ''c'' to indicate I guessed correctly. ')
    
    if boundary == 'c':
        break

    if boundary != 'h' and boundary != 'l':
        print 'Sorry, I did not understand your input.'
    elif boundary == 'l':
       lowerEnd = guess
    elif boundary == 'h':
        higherEnd = guess

print 'Game over. Your secret number was: ' + str(guess)

##################################

## ii it a vowel #################

def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for n in vowels:
        if char == n: 
            return True
    return False

#################################

### polysum ####################

import math

def polysum(n, s):
    
    area = (0.25*n*s**2)/math.tan(math.pi/n)
    perimeter = s*n
    
    return round(area + perimeter**2, 4)

################################

## Week 3

## iterative exponantian

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    res = 1
    
    while exp > 0:
        res = res * base
        exp -= 1
    return res

## recursive exponantian

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 1:
        return base
    elif exp == 0:
        return 1
    else:
        return base * recurPower(base, exp-1)

# using multiplication

def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    if exp == 0:
        return 1
    elif exp % 2 != 0:
        return base * recurPowerNew(base, exp-1)
    else:
        return recurPowerNew(base * base, exp/2)

# iterative greatest common divisor

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a < b:
        t = a
    else:
        t = b
    
    while t != 0:
    
        if t == 1:
            return 1
        elif a % t == 0 and b % t == 0:
            return t
        
        t -= 1

# recusrsive greatest common divisor

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

# own length function

def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    length = 0
    
    for l in aStr:
        length += 1
    
    return length

# recursive length function

def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    
    if aStr == '':
        return 0
    else:
        return 1 + lenRecur(aStr[:-1])

# is a character i a string (recursive)

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr == '':
        return False
    elif len(aStr) == 1:
        if char == aStr:
            return True
        else:
            return False
    elif len(aStr) > 1:
        if char == aStr[-1]:
            return True
        else:
            return isIn(char, aStr[:-1])

#  semordnilap

# missing



def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    return aTup[::2]

###
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

# list version

def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

#### count animals in a dict

def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count = 0
    for e in aDict.values():
       for a in e: count += 1
    
    return count
   
   #return sum(len(v) for v in aDict.values())

### find key with the biggest value i a dict (not working)

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    if len(aDict) < 1:
        return None
    else:   
        valList = []
        for e in aDict.values():
            count = 0
            for a in e:
               count += 1
               valList.append(count)
    maxEntry = max(valList)

    #Version B
    return [k for k, v in aDict.values() if v == maxEntry]

    #Version C - finds the key with the max value
    def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    
    if len(aDict) < 1:
        return None
    else:
    
        return max(aDict, key=aDict.get))

## Week 4

def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0
    
    while x >= a:
        count += 1
        x = x - a
    return count

def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        rem(x-a, a)

def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      return n
   else:
      return n * f(n-1)

def SimpleDivide(item, denom):
   try:
       return item / denom
   except ZeroDivisionError, e:
       return 0

## Week 5 - compexity of growth

def linearSearch(L, x):
    for e in L:
        if e == x:
            return True
    return False

def program1(x):
    total = 0
    for i in range(1000):
        total += i

    while x > 0:
        x -= 1
        total += x

    return total

def program2(x):
    total = 0
    for i in range(1000):
        total = i

    while x > 0:
        x /= 2
        total += x

    return total

def program3(L):
    totalSum = 0
    highestFound = None
    for x in L:
        totalSum += x

    for x in L:
        if highestFound == None:
            highestFound = x
        elif x > highestFound:
            highestFound = x

    return (totalSum, highestFound)

def program1(L):
    multiples = []
    for x in L:
        for y in L:
            multiples.append(x*y)
    return multiples

def program2(L):
    squares = []
    for x in L:
        for y in L:
            if x == y:
                squares.append(x*y)
    return squares

def program3(L1, L2):
    intersection = []
    for elt in L1:
        if elt in L2:
            intersection.append(elt)
    return intersection

def lenRecur(s):
   if s == '':
      return 0
   else:
      return 1 + lenRecur(s[1:])

def isIn(a, s):
   '''
   a is a character, or, singleton string.
   s is a string, sorted in alphabetical order.
   '''
   if len(s) == 0:
      return False
   elif len(s) == 1:
      return a == s
   else:
      test = s[len(s)/2]
      if test == a:
         return True
      elif a < test:
         return isIn(a, s[:len(s)/2])
      else:
         return isIn(a, s[len(s)/2+1:])

def union(L1, L2):
   '''
   L1 & L2 are lists of the same length, n
   '''
   temp = L1[:]
   for e2 in L2:
      flag = False
      for check in temp:
         if e2 == check:
            flag = True
            break
      if not flag:
         temp.append(e2)
   return temp

def unionNew(L1, L2):
   '''
   L1 & L2 are lists of the same length, n
   '''
   temp = []
   for e1 in L1:
      flag = False
      for e2 in L2:
         if e1 == e2:
            flag = True
            break
      if not flag:
         temp.append(e1)
   return temp + L2

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def search1(L, e):
    for i in L:
        if i == e:
            return True
        if i > e:
            return False
    return False

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def search2(L, e):
    for i in L:
        if i == e:
            return True
        elif i > e:
            return False
    return False

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def search3(L, e):
    if L[0] == e:
        return True
    elif L[0] > e:
        return False
    else:
        return search3(L[1:], e)

def selSort(L):
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        j = i+1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        if minIndx != i:
            temp = L[i]
            L[i] = L[minIndx]
            L[minIndx] = temp

def newSort(L):
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1

def mySort(L):
    clear = False
    while not clear:
        clear = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                clear = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp

def newSort(L):
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1

## hash functions

def hash(s):
    return string.ascii_lowercase.index(s[0])

def hash(s):
    return string.ascii_lowercase.index(s[-1])

def hash(s):
    total = 0
    for char in s:
        total += string.ascii_lowercase.index(char)
    return total % 26

# Week 6 - object orientation

class Clock(object):
    def __init__(self, time):
	self.time = time
    def print_time(self):
	time = '6:30'
	print self.time

clock = Clock('5:30')
clock.print_time()

class Clock(object):
    def __init__(self, time):
	self.time = time
    def print_time(self, time):
	print time

clock = Clock('5:30')
clock.print_time('10:30')

class Clock(object):
    def __init__(self, time):
	self.time = time
    def print_time(self):
	print self.time

boston_clock = Clock('5:30')
paris_clock = boston_clock
paris_clock.time = '10:30'
boston_clock.print_time()

class Weird(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return x 
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return self.x 
    def getY(self):
        return self.y

X = 7
Y = 8

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    
    def __eq__(self, other):
        assert type(other) == type(self)
        return self.getX() == other.getX() and self.getY() == other.getY()

    
    def __repr__(self):
        return 'Coordinate(' + str(self.getX()) + ', ' + str(self.getY()) + ')'
        
class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()
              
    def getDescription(self):
        return 'No description'
    
    def execute(self):
        print self.incantation    


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'

def studySpell(spell):
    print spell

spell = Accio()
spell.execute()
studySpell(spell)
studySpell(Confundo())

class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')
    
    def __str__(self):
       return self.name + ' ' + self.incantation + '\n' + self.getDescription()
              
    def getDescription(self):
        return 'This charm summons an object to the caster, potentially over a significant distance.'

    class A(object):
    def __init__(self):
        self.a = 1
    def x(self):
        print "A.x"
    def y(self):
        print "A.y"
    def z(self):
        print "A.z"

class B(A):
    def __init__(self):
        A.__init__(self)
        self.a = 2
        self.b = 3
    def y(self):
        print "B.y"
    def z(self):
        print "B.z"

class C(object):
    def __init__(self):
        self.a = 4
        self.c = 5
    def y(self):
        print "C.y"
    def z(self):
        print "C.z"

class D(C, B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = 6
    def z(self):
        print "D.z"

# Hand from ProblemSet 3 as object

import random 

class Hand(object):
    def __init__(self, n):
        '''
        Initialize a Hand.

        n: integer, the size of the hand.
        '''
        assert type(n) == int
        self.HAND_SIZE = n
        self.VOWELS = 'aeiou'
        self.CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

        # Deal a new hand
        self.dealNewHand()

    def dealNewHand(self):
        '''
        Deals a new hand, and sets the hand attribute to the new hand.
        '''
        # Set self.hand to a new, empty dictionary
        self.hand = {}

        # Build the hand
        numVowels = self.HAND_SIZE / 3
    
        for i in range(numVowels):
            x = self.VOWELS[random.randrange(0,len(self.VOWELS))]
            self.hand[x] = self.hand.get(x, 0) + 1
        
        for i in range(numVowels, self.HAND_SIZE):    
            x = self.CONSONANTS[random.randrange(0,len(self.CONSONANTS))]
            self.hand[x] = self.hand.get(x, 0) + 1
            
    def setDummyHand(self, handString):
        '''
        Allows you to set a dummy hand. Useful for testing your implementation.

        handString: A string of letters you wish to be in the hand. Length of this
        string must be equal to self.HAND_SIZE.

        This method converts sets the hand attribute to a dictionary
        containing the letters of handString.
        '''
        assert len(handString) == self.HAND_SIZE, "Length of handString ({0}) must equal length of HAND_SIZE ({1})".format(len(handString), self.HAND_SIZE)
        self.hand = {}
        for char in handString:
            self.hand[char] = self.hand.get(char, 0) + 1


    def calculateLen(self):
        '''
        Calculate the length of the hand.
        '''
        ans = 0
        for k in self.hand:
            ans += self.hand[k]
        return ans
    
    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''
        hand_keys = self.hand.keys()
        hand_keys.sort()
        for letter in hand_keys:
            for j in range(self.hand[letter]):
                output += letter
        return output

    def update(self, word):
        """
        Does not assume that self.hand has all the letters in word.

        Updates the hand: if self.hand does have all the letters to make
        the word, modifies self.hand by using up the letters in the given word.

        Returns True if the word was able to be made with the letter in
        the hand; False otherwise.
        
        word: string
        returns: Boolean (if the word was or was not made)
        """
        used = 0

        for e in range(len(word)):
            for f in range(len(self.hand.keys())):
                if self.hand.keys()[f] == word[e]:
                    self.hand[self.hand.keys()[f]] -= 1
                    used += 1
                    if self.hand[self.hand.keys()[f]] == 0:
                        self.hand.pop(self.hand.keys()[f], 0)
                    break

        if used == len(word):
            return True
        else:
            return False
########################################
        
def genPrimes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}
    
    # The running integer that's checked for primeness
    q = 2
    
    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        
        q += 1

## Week 7

#trees


