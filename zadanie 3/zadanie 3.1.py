plik = open('dane3.txt', 'r')
linijki = plik.readlines()

przedzial=[]
dlugosci = []

for linijka in linijki:
    linijka = linijka.strip().split()
    a = int(linijka[0])
    b = int(linijka[1])

    dlugosc = b - a + 1
    dlugosci.append(dlugosc)
    dlugosci.sort()

    przedzial.append((a, b))







print(dlugosci[0],dlugosci[1])