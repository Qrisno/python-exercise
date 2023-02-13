#Exercise 3


def calculateArea(w, l):
    return int(w) * int(l)

length  = input("What is length?")
width  = input("What is width?")

print("Room Area is " + str(calculateArea(width, length)))