fh=open("handheld.txt","r")

for line in fh:
    transmission = line
    for i in range(len(transmission)):
        startof=transmission[i:i+14]
        if len(set(startof)) == len(startof):
            print(i+14)
            break