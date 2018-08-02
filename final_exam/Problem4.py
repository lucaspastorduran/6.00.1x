from collections import Counter

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    # Count times ach element appears
    elements_frequency = dict(Counter(L))
    # Get the maximum of elements that only appear Odd times
    maximum = None
    for k, v in elements_frequency.items():
        if v%2 != 0:
            # element appears odd times
            if maximum is None or k > maximum:
                maximum = k
    return maximum

def testLargestOdd(L):
    print("testing largest_odd_times on {}".format(L))
    print(largest_odd_times(L))

if __name__ == "__main__":
    lists_to_test = [[], [1], [2], [1, 2], [2, 3], [1,2,3,4], [5,6,7,8,9], [2,2,4,4], [3,9,5,3,5,3]]
    for L in lists_to_test:
        testLargestOdd(L)
