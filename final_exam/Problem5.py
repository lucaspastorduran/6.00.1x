def f(n1, n2):
    return n1 + n2

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    intersection, difference = {}, {}
    for key, value in d1.items():
        if key in d2:
            intersection[key] = f(value, d2[key])
        else:
            difference[key] = value
    for key, value in d2.items():
        if key not in d1:
            difference[key] = value
    return (intersection, difference)

def testDictInterDiff(f, d1, d2):
    print("testing {} on '{}' and '{}'".format(f, d1, d2))
    print(f(d1, d2))

if __name__ == "__main__":
    dicts_to_test = [{1:30, 2:20, 3:30, 5:80}, {1:40, 2:50, 3:60, 4:70, 6:90}, {1:30, 2:20, 3:30}, {1:40, 2:50, 3:60}]
    for d1 in dicts_to_test:
        for d2 in dicts_to_test:
            testDictInterDiff(dict_interdiff, d1, d2)
