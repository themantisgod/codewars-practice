import sys
f = open(r"input14.txt", "r") #use RELATIVE paths!
count = 0
newList = []
for line in f:
    useLine = line.split()
    if "CheckSum" not in useLine[0]:
        for thing in useLine:
            try: 
                floatThing = float(thing)
                newList.append(floatThing) 
            except:
                continue
        for each in newList:
            count += each
            if int(each) == each:
                sys.stdout.write(str(int(each)) + " ")
            else:
                sys.stdout.write(str(each) + " ")   
    else:
        print("")
        checkLine = line.split("=")
        checkSum = checkLine[1]
        if checkSum == str(count):
            print("CHECKED")
        else:
            print("BADCHECK: " + str(count))    
