import math

def numOfBusses(s):
    total = s/52
    if total.is_integer() == True:
        return int(total)
    else:
        return math.ceil(total)

print(numOfBusses(156))