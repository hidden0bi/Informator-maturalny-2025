file = open('dane8.txt','r')
lines = file.readlines()
list = []

for line in lines:
    line = int(line.strip())
    list.append(line)

count = 0
for i in range(len(list)):
    for j in range(len(list)):
        if list[i] > list[j] and i < j:
            count += 1

print(count)
#hehe