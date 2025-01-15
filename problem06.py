import sys
f = open(r"input06.txt", "r") #use RELATIVE paths!
for line in f:
    useLine = line.split()
    try:
        monthsOld = (int(useLine[1]) * 12) + int(useLine[2])
        monthsNeeded = (25 * 12) - monthsOld
        print(useLine[0] + " " + str(monthsNeeded))
    except Exception as e:
        print(e) 