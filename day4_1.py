import re
fh = open("assignments.txt", "r")
score=0
for line in fh:
    assign = line.strip()
    re_assign = re.split(",|-", assign)
    ass_1 = range(int(re_assign[0]),int(re_assign[1])+1)
    ass_2 = range(int(re_assign[2]),int(re_assign[3])+1)
    #print(ass_1, ass_2)
    elf1 = ""
    for i in ass_1:
        elf1 += " "+str(i)+","
    #print(elf1)
    elf2 = ""
    for j in ass_2:
        elf2 += " "+str(j)+","
    #print(elf2)
    if elf2 in elf1:
        score += 1
        print(ass_1, ass_2)
        print(elf1)
        print(elf2)
        print("score: ", score)
        continue
    if elf1 in elf2:
        score += 1
        print(ass_1, ass_2)
        print(elf1)
        print(elf2)
        print("score: ", score)
        continue
print(score)