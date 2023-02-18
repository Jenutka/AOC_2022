fh=open("handheld.txt","r")

for line in fh:
    transmission = line
    for i in range(len(transmission)):
        startof=transmission[i]+transmission[i+1]+transmission[i+2]+transmission[i+3]
        if len(set(startof)) == len(startof):
            print(i+4)
            break
        if i == len(transmission)-4:
            break