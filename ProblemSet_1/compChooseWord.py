
#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    
    SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }
    
    def handToString(hand):

        handStringList = []
    
        # convert hand form dic into list
        for letter in hand.keys():
            for j in range(hand[letter]):
                 handStringList.append(letter)

        handString = ''.join(handStringList)
        return handString

    def isStringinString(handString, l):
        
        if handString.find(l) != -1:
            hit = 1
            handString.replace(word[l], '', 1)
        else:
            hit = 0

        return hit

    def getWordScore(word, n):
        """
        Returns the score for a word. Assumes the word is a valid word.

        The score for a word is the sum of the points for letters in the
        word, multiplied by the length of the word, PLUS 50 points if all n
        letters are used on the first turn.

        Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
        worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

        word: string (lowercase letters)
        n: integer (HAND_SIZE; i.e., hand size required for additional points)
        returns: int >= 0
        """

        score = 0
    
        for e in range(len(word)):
            for f in range(len(SCRABBLE_LETTER_VALUES.keys())):
                if SCRABBLE_LETTER_VALUES.keys()[f] == word[e]:
                    score = score + SCRABBLE_LETTER_VALUES[SCRABBLE_LETTER_VALUES.keys()[f]]
                    break

        if len(word) == n:
            return score*len(word) + 50
        else:
            return score*len(word)
        
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    endWord = None

    handString = handToString(hand)
    handSize = len(handString)

    # For each word in the wordList
    allHits = 0
    for word in wordList:
        for l in word:
            print l
            hit = isStringinString(handString, l)
            allHits += hit
            break

        # If you can construct the word from your hand
        if allHits == len(word):
            # Find out how much making that word is worth
            wordScore = getWordScore(word, handSize)
        else:
            wordScore = 0
            
        # If the score for that word is higher than your best score
        if wordScore > maxScore:
            # Update your best score, and best word accordingly
            maxScore = wordScore
            endWord = word      

    # return the best word you found.
    return endWord
