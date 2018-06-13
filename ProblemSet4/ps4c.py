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
    #hand_len = calculateHandlen(hand)
    #print("Starting with hand with {} letters:\n{}".format(hand_len, hand))
    # if there are no more letters, we finished
    words_and_scores = [["",0]]
    if calculateHandlen(hand) <= 0:
        return words_and_scores
    else:
        # we still have more letters, check if there are more combinations
        hand_possible_paths = []
        for word in wordList:
            # If you can construct the word from your hand
            if isValidWord(word, hand, wordList):
                word_score = getWortdScore(word, n)
                path = [[word, word_score]]
                #print("Found a valid word '{}'. With score {}".format(word, word_score))
                # find out how much making that word is worth
                remaining_hand = updateHand(hand, word)
                #print("remaining hand:", remaining_hand)
                path.extend(skynetChooseWord(remaining_hand, wordList, n))
                hand_possible_paths.append([word, score])
        # Choose the word with the highest score and play that hand
        #if len(words_and_scores) > 1:
            #print("All the words and scores found are:", words_and_scores)
        words_and_scores.sort(key=lambda x: x[1], reverse = True)
        word = words_and_scores[0][0]
        score = words_and_scores[0][1]
        #if len(words_and_scores) > 1:
        #    print("From all the words seen in hand {}, {} was the best with score {}".format(hand,word, score))
        return words_and_scores


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
        if word == 'NotAValidResult':
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

  