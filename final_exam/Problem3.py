def laceStringsRec(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    if not s1 or not s2:
        return s1 + s2
    else:
        return s1[0] + s2[0] + laceStrings(s1[1:], s2[1:])

def laceStrings(s1, s2):
    result = ''
    for i in range(max(len(s1), len(s2))):
        if i >= len(s1):
            result += s2[i]
        elif i >= len(s2):
            result += s1[i]
        else:
            result += s1[i] + s2[i]
    return result

def testLaceStrings(s1, s2):
    print("testing laceStrings on '{}' and '{}'".format(s1, s2))
    print(laceStrings(s1, s2))

if __name__ == "__main__":
    strings_to_test = ['', 'A', ',.', '1234', 'abcdef']
    for s1 in strings_to_test:
        for s2 in strings_to_test:
            testLaceStrings(s1, s2)
