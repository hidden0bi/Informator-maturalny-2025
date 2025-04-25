#KOD JEST BLĘDNY, W CZASIE ROBIENIA GO DOSTALEM KURWY!
file = open('dane8.txt','r')
lines = file.readlines()
list = []

for line in lines:
    line = int(line.strip())
    list.append(line)

n = [1] * n

max_length = 0
length = 1
length_temp = 1


for i in range(1, len(list)):
    if list[i-1] < list[i]:
        length += 1
    else:
        length = 1
    for j in range(i):
        if list[j] < list[i]:
            if dl[j] + 1 > dl[i]:
                dl[i] = dl[j] + 1

            i = i+1
    if length > max_length:
        max_length = length


print(max_length)

