def checkLeapyear(y):
    result = ""
    if y % 4 == 0:
        if y % 100 == 0 and y % 400 != 0:
            result = "No, this year is not a leap year."
        else:
            result = "Yes, this year is a leap year."
    else:
        result = "No, this year is not a leap year."
    return result

print(checkLeapyear(2000))