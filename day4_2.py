import re
fh = open("assignments.txt", "r")
score=0
for line in fh:
    assign = line.strip()
    re_assign = re.split(",|-", assign)
    ass_1 = range(int(re_assign[0]),int(re_assign[1])+1)
    ass_2 = range(int(re_assign[2]),int(re_assign[3])+1)
    elf1 = []
    for item in ass_1:
        elf1.append(item)
    elf2 = []
    for item in ass_2:
        elf2.append(item)
    set1 = set(elf1)
    set2 = set(elf2)
    newlist = list(set1.intersection(set2))
    if len(newlist) > 0:
        score += 1

print(score)