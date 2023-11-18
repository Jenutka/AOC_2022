import re

stack_1=["S", "M", "R", "N", "W", "J", "V", "T"]
stack_2=["B", "W", "D", "J", "Q", "P", "C", "V"]
stack_3=["B", "J", "F", "H", "D", "R", "P"]
stack_4=["F", "R", "P", "B", "M", "N", "D"]
stack_5=["H", "V", "R", "P", "T", "B"]
stack_6=["C", "B", "P", "T"]
stack_7=["B", "J", "R", "P", "L"]
stack_8=["N", "C", "S", "L", "T", "Z", "B", "W"]
stack_9=["L", "S", "G"]

stacks={1:stack_1, 2:stack_2, 3:stack_3, 4:stack_4, 5:stack_5,
        6:stack_6, 7:stack_7, 8:stack_8, 9:stack_9}

top_items = ""
fh = open("rearrangement.txt", "r")
for line in fh:
    moves = line.strip()
    re_moves = re.split("move | from | to ", moves)
    re_moves.remove("")
    re_moves = list(map(int, re_moves))
    items=stacks[re_moves[1]][-re_moves[0]:]
    for i in items:
        stacks[re_moves[2]].append(i)
    del stacks[re_moves[1]][-re_moves[0]:]

for values in stacks.values():
    top_items += values[-1]

print(top_items)
