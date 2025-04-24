file = open('czestosc.txt','r')
lines = file.readlines()

slownik = {}

for line in lines:
    line = line.strip()
    line = line.split()
    letter = line[0]
    number = line[1]
    slownik[letter] = number
print(slownik)

