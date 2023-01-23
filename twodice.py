import random

def twodice():
    ran1 = random.randint(1, 6)
    ran2 = random.randint(1, 6)
    result = ""
    ranSum = 0
    if ran1 + ran2 >= 6 and ran1 + ran2 <= 8:
        result = "You lose!"
    else:
        result = "You win!"
    return result

print(twodice())