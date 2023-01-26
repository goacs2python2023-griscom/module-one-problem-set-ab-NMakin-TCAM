def tipcalculator(b, p):
    multPercentage = p/100 + 1
    total = b*multPercentage
    return total

print(tipcalculator(1, 6))