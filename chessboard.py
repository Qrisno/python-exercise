#Exercise 17
letterDictionary = {
    'a': False,
    'b': True,
    'c': False,
    'd': True,
    'e': False,
    'f': True,
    'g': False,
    'h': True,
}

def getSquareState(position):
    letter = list(position)[0]
    num= list(position)[1]

    letterIsEven = letterDictionary[letter]
    numIsEven = int(num) % 2 == 0

    if letterIsEven and numIsEven:
        return "Black"
    if not letterIsEven and not numIsEven:
        return "Black"
    else:
        return "White"

position = input("Enter a posistion on a checkboard")

print(getSquareState(position))

