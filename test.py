def getKey(item):
    return int(item[0])

#make a list with lines of file
l = []
file = open("highscores.txt", "r")
for line in file:
    l.append(line)

#convert list of lines to list of partitions
for i in range(len(l)):
        l[i] = l[i][:-1]
        l[i] = l[i].partition(" ")

for a in l:
    print(a[0])

for a in l:
    print(a[2])

l.sort(key=getKey, reverse=True)
#min(l, key=getKey)
print(l)
    
