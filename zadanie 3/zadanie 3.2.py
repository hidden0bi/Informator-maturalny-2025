plik = open('dane3.txt', 'r')
linijki = plik.readlines()
dlugosci = []
slownik = {}

for linijka in linijki:
    linijka = linijka.strip().split()
    a = int(linijka[0])
    b = int(linijka[1])
    dlugosc = b - a + 1


    if dlugosc not in slownik:
        slownik[dlugosc] = 1
    else:
        slownik[dlugosc] += 1
    posortowane = dict(sorted(slownik.items(), key=lambda item: item[1],reverse=True)) #ten  key=lambda item: item[1] odpowiada za to ktory item wybierze, bo [0] to klucz, a [1] to wartosc

print(posortowane)