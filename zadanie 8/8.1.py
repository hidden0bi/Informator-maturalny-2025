file = open('dane8.txt','r')
lines = file.readlines()
list = []
even = 0
odd = 0
for line in lines:
    line = int(line.strip())
    list.append(line)

for i in range(1, len(list)):
    loophole = abs(list[i] - list[i-1])
    if loophole % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'Parzystych: {even}, nieparzystych: {odd}')
#hehe