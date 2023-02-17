#!/usr/local/bin/python

fh = open("calories.txt", "r")
elves = []
total = 0

for cal in fh:
    if cal=='\n':
        elves.append(total)
        total = 0
#        print(total)
    else:
#        print(total)
        total += int(cal)

print(elves)
print(max(elves))

