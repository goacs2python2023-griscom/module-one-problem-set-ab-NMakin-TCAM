def findEarlierDate(m1, d1, y1, m2, d2, y2):
    result = ""
    if y1 > y2:
        result = "After"
    elif y1< y2:
        result = "Before"
    else:
        if m1 > m2:
            result = "After"
        elif m1< m2:
            result = "Before"
        else:
            if d1 > d2:
                result = "After"
            elif d1< d2:
                result = "Before"
            else:
                result = "They are the same date"
    return result

print(findEarlierDate(1, 2, 3, 2, 2, 3))