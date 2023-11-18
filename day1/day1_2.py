#!/usr/local/bin/python

fh = open("calories.txt", "r")
elves = []
total = 0

for cal in fh:
    if cal=='\n':
        elves.append(total)
        total = 0
    else:
        total += int(cal)

print(elves)
top_three = 0
top_index = int(elves.index(max(elves)))
top_three += elves.pop(top_index)
top_index = int(elves.index(max(elves)))
top_three += elves.pop(top_index)
top_index = int(elves.index(max(elves)))
top_three += elves.pop(top_index)
print(top_three)

#fugitive testing
