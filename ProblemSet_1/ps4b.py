from ps4a import *
import time


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
       
    def handToString(hand):

        handStringList = []
    
        # convert hand form dic into list
        for letter in hand.keys():
            for j in range(hand[letter]):
                 handStringList.append(letter)

        handString = ''.join(handStringList)

        return handString
      
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    endWord = None

    # For each word in the wordList   
    for word in wordList:

        handString = handToString(hand)
        #print handString
        handSize = len(handString)
        #print handSize
        allHits = 0
        #print word

        for l in word:
            #print l
            if handString.find(l) != -1:
                allHits += 1
                handString = handString.replace(l, '', 1)
                #print handString
            #break

        # If you can construct the word from your hand
        if allHits == len(word):
            # Find out how much making that word is worth
            wordScore = getWordScore(word, handSize)
            #print wordScore
        else:
            wordScore = 0
            
        # If the score for that word is higher than your best score
        if wordScore > maxScore:
            # Update your best score, and best word accordingly
            maxScore = wordScore
            #print maxScore
            endWord = word
            #print endWord

    # return the best word you found.
    return endWord

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """

    def displayHand2(hand):
        
        stringList = []

        for letter in hand.keys():
            for j in range(hand[letter]):
                 stringList.append(letter)
                 stringList.append(' ')

        stringList = ''.join(stringList)
        
        return stringList

    def updateHand2(hand, word):
        """
        Assumes that 'hand' has all the letters in word.
        In other words, this assumes that however many times
        a letter appears in 'word', 'hand' has at least as
        many of that letter in it. 

        Updates the hand: uses up the letters in the given word
        and returns the new hand, without those letters in it.

        Has no side effects: does not modify hand.

        word: string
        hand: dictionary (string -> int)    
        returns: dictionary (string -> int)
        """

        copyHand = hand.copy() 
        
        for e in range(len(word)):
            for f in range(len(copyHand.keys())):
                if copyHand.keys()[f] == word[e]:
                    copyHand[copyHand.keys()[f]] -= 1
                    if copyHand[copyHand.keys()[f]] == 0:
                        copyHand.pop(copyHand.keys()[f], 0)
                    break

        return copyHand

    def compChooseWord(hand, wordList, n):
           
        def handToString(hand):

            handStringList = []
    
            # convert hand form dic into list
            for letter in hand.keys():
                for j in range(hand[letter]):
                     handStringList.append(letter)

            handString = ''.join(handStringList)

            return handString
      
        # Create a new variable to store the maximum score seen so far (initially 0)
        maxScore = 0
        # Create a new variable to store the best word seen so far (initially None)  
        endWord = None

        # For each word in the wordList   
        for word in wordList:

            handString = handToString(hand)
            #print handString
            handSize = len(handString)
            #print handSize
            allHits = 0
            #print word

            for l in word:
                #print l
                if handString.find(l) != -1:
                    allHits += 1
                    handString = handString.replace(l, '', 1)
                    #print handString
                #break

            # If you can construct the word from your hand
            if allHits == len(word):
                # Find out how much making that word is worth
                wordScore = getWordScore(word, handSize)
                #print wordScore
            else:
                wordScore = 0
            
            # If the score for that word is higher than your best score
            if wordScore > maxScore:
                # Update your best score, and best word accordingly
                maxScore = wordScore
                #print maxScore
                endWord = word
                #print endWord

        # return the best word you found.
        return endWord

    # Keep track of the total score
    totalScore = 0
    
    # As long as there are still letters left in the hand:
    while hand:
        
        # Display the hand
        print 'Current Hand: ', displayHand2(hand)
        
        # let computer find a word
        word = compChooseWord(hand, wordList, n)
        # If the input is a single period:
        if word == None:
            # End the game (break out of the loop)
            break    
        # Otherwise (the input is not a single period):
        else:

            wordScore = getWordScore(word, n)
            totalScore += wordScore
                
            # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
            print '"' + str(word) + '"' + ' earned ' + str(wordScore) + ' points. Total: ' + str(totalScore) + '\n'
            # Update the hand 
            hand = updateHand2(hand, word)

    # Game is over (computer cannot find any more words with the hand)
    print 'Total score: ' + str(totalScore) + '.'
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """

    n = HAND_SIZE
    #wordList = loadWords()
    #hand = {'d': 1, 'e': 1, 'f': 1, 'a': 1, 'l': 1, 't': 1}
    hand = 0
    game = 1
    
##    while game:
##        mode = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
##                                   
##        if mode == 'n':
##            player = raw_input('Enter u to have yourself play, c to have the computer play: ')
##            if player == 'u':
##               hand = dealHand(n)
##               playHand(hand, wordList, n)
##            elif player == 'c':
##               hand = dealHand(n)
##               compPlayHand(hand, wordList, n)
##            else:
##               print 'Invalid command.'          
##        elif mode == 'r':
##            if hand:
##               hand = hand
##               player = raw_input('Enter u to have yourself play, c to have the computer play: : ')
##               if player == 'u':
##                  playHand(hand, wordList, n)
##               elif player == 'c':
##                  compPlayHand(hand, wordList, n)
##               else:
##                  print 'Invalid command.'
##            else:
##                print 'You have not played a hand yet. Please play a new hand first!'
##        elif mode == 'e':
##            return
##        else:
##            print 'Invalid command.'

    while game:
        mode = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
                                   
        if mode == 'n':
            while mode == 'n':
                player = raw_input('Enter u to have yourself play, c to have the computer play: ')
                if player == 'u':
                    hand = dealHand(n)
                    playHand(hand, wordList, n)
                    break
                elif player == 'c':
                    hand = dealHand(n)
                    compPlayHand(hand, wordList, n)
                    break
                else:
                    print 'Invalid command.'          
        elif mode == 'r':
            if hand:
                while mode == 'r':
                    hand = hand
                    player = raw_input('Enter u to have yourself play, c to have the computer play: : ')
                    if player == 'u':
                        playHand(hand, wordList, n)
                        break
                    elif player == 'c':
                        compPlayHand(hand, wordList, n)
                        break
                    else:
                         print 'Invalid command.'
            else:
                print 'You have not played a hand yet. Please play a new hand first!'
        elif mode == 'e':
            return
        else:
            print 'Invalid command.'
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


