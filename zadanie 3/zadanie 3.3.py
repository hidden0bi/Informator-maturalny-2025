plik = open('dane3.txt', 'r')
linijki = plik.readlines()

przedzialy = []

for linijka in linijki:
    linijka = linijka.strip().split()
    a = int(linijka[0])
    b = int(linijka[1])
    przedzialy.append((a, b))

przedzialy.sort(key=lambda x: (x[1] - x[0], x[0]))
najdluzsze_lancuchy = [1] * len(przedzialy)



lancuch_przedzialow = 0
max_lancuch = 0

for i in range(len(przedzialy)):
    for j in range(i):
        if przedzialy[i][0] <= przedzialy[j][0] and przedzialy[j][1] <= przedzialy[i][1]:
            if najdluzsze_lancuchy[j] + 1 > najdluzsze_lancuchy[i]:
                najdluzsze_lancuchy[i] = najdluzsze_lancuchy[j] + 1

print((max(najdluzsze_lancuchy)))