"""Alotting jersey numbers to NFL positions"""

def jersey_check(number):
    if (number >= 1 and number <= 19):
        pos = "QB"
    elif (number >= 20 and number <= 39):
        pos = "RB"
    elif ((number >= 40 and number <= 49) or (number >= 80 and number <= 89)):
        pos = "TE"
    elif ((number >= 50 and number <= 59) or (number >= 90 and number <= 99)):
        pos = "LB"
    else:
        pos = "Invalid #"
    return pos

num = int(input("Please enter the number you would like to check: "))
print(jersey_check(num))
