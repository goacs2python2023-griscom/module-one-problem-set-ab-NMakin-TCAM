def checkForDupe(l):
    dupeCount = False
    for n in l:
        if int(l.count(n)) > 1:
            dupeCount = True
    return dupeCount

def raceMedals(y, o1, o2, o3):
    medal = ""
    times = [y, o1, o2, o3]
    times.sort()
    if checkForDupe(times) == True:
        medal = "We cannot have ties in this competition.  Let's do a tie-breaker to finalize the leaderboard."
    elif times[0] == y:
        medal = "Gold medal, yeah!"
    elif times[1] == y:
        medal = "Silver medal, great work out there!"
    elif times[2] == y:
        medal = "Bronze medal, not bad!"
    elif times[3] == y:
        medal = "No medal, sorry."
    return medal

#Insert your time in minutes
print(raceMedals(3, 2, 3, 1))
print(raceMedals(67, 49, 66, 14))
print(raceMedals(1, 4, 3, 2))
