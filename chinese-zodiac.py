#Exercise 18

zodiacYears = {
    0 : "Dragon",
    1 :"Snake",
    2 :"Horse",
    3 :"Sheep",
    4: "Monkey",
    5: "Rooster",
    6: "Dog",
    7 :"Pig",
    8 :"Rat",
    9 :"Ox",
    10 :"Tiger",
    11 :"Hare"
}


def getYearZodiac(year):
    difference = (int(year) - 2000) % 12

    return zodiacYears[difference]


year = input("year: ")

print(getYearZodiac(year))

