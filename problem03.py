import sys
f = open(r"input03.txt", "r") #use RELATIVE paths!
for line in f:
    num = int(line.rstrip())
    if num == -1:
        break
    elif num == 1:
        print("You, 1 minute ago.")
    else:
        print("You, " + str(num) + " minutes ago.")
