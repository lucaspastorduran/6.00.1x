from ps4b import *


#
# Computer plays a hand in an extreme way
#
def skynetChooseWord(hand, wordList, n):
    """
    Allows the computer to play the given hand, following another procedure
    than in compPlayHand. Looks at all the possible combinations given a hand
    and all the possible paths. Once done, chooses the path with better score.

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
    hand_len = calculateHandlen(hand)
    print("\nStarting with hand with {} letters:\n{}".format(hand_len, hand))
    # if there are no more letters, we finished
    words_and_scores = [[[''],0]]
    if calculateHandlen(hand) <= 0:
        return words_and_scores
    else:
        # we still have more letters, check if there are more combinations
        for word in wordList:
            # If you can construct the word from your hand
            if isValidWord(word, hand, wordList):
                print("Found valid word:", word)
                # find out how much making that word is worth
                remaining_hand = updateHand(hand, word)
                print("remaining hand:", remaining_hand)
                # check what words and scores can we get with remaining hand
                hand_possible_paths = skynetChooseWord(remaining_hand, wordList, n)
                print("Possible games after current hand:\n", hand_possible_paths)
                # add the current word and score to result found
                hand_possible_paths[0].insert(0, word)
                hand_possible_paths[1] += getWordScore(word, n)
                print("Possible games after current hand including word:\n", hand_possible_paths)
                # store it in words_and_scores to later see if its the best solution
                words_and_scores.append(hand_possible_paths)
        # Choose the word with the highest score and play that hand
        words_and_scores.sort(key=lambda x: x[1], reverse = True)
        if len(words_and_scores) > 1:
            print("All the words and scores found are:", words_and_scores)
        return words_and_scores[0]


#
# Computer plays a hand
#
def skynetPlayHand(hand, wordList, n):
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
    # Keep track of the total score
    totalScore = 0
    # As long as there are still letters left in the hand:
    while (calculateHandlen(hand) > 0) :
        # Display the hand
        displayHand(hand)
        # computer's word
        word = skynetChooseWord(hand, wordList, n)[0]
        # If the input is a single period:
        if word == '':
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not a single period):
        else :
            # If the word is not valid:
            if (not isValidWord(word, hand, wordList)) :
                print('This is a terrible error! I need to check my own code!')
                break
            # Otherwise (the word is valid):
            else :
                # Tell the user how many points the word earned, and the updated total score 
                score = getWordScore(word, n)
                totalScore += score
                print('"' + word + '" earned ' + str(score) + ' points. Total: ' + str(totalScore) + ' points')              
                # Update hand and show the updated hand to the user
                hand = updateHand(hand, word)
                #print()
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print('Total score: ' + str(totalScore) + ' points.')

  