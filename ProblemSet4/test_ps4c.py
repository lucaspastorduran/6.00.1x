from ps4c import *


def test_skynetChooseWord():
    print("Starting SkyNet chooseWord with hand", hand)
    skynetWords = skynetChooseWord(hand, wordList, len_hand)    
    print(skynetWords)
    #SkyNetPlayHand({'h':1, 'i':1, 'c':1, 'z':1, 'm':2, 'a':1}, wordList, 7)


def test_skynetPlayHand(hand, wordList, n):
    print("Starting Skynet play hand")
    skynetPlayHand(hand, wordList, n)

if __name__ == '__main__':
    wordList = loadWords()[0::50]
    wordList.extend(['tarantula', 'scorpion', 'haters', 'axis'])
    word = "hatersaxi"
    hand = getFrequencyDict(word)
    len_hand = calculateHandlen(hand)
    test_skynetPlayHand(hand, wordList, len_hand)
    print('\nStarting 6.00.1x computer hand')
    compPlayHand(hand, wordList, len_hand)
    #test_skynetChooseWord()