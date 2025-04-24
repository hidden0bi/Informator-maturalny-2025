file = open('dane8.txt','r')
lines = file.readlines()
list = []

for line in lines:
    line = int(line.strip())
    list.append(line)

max_length = 0
length = 1


for i in range(1, len(list)):
    if list[i-1] < list[i]:
        length += 1
        if length > max_length:
            max_length = length
    else:
        length = 1

print(max_length)
#hehe