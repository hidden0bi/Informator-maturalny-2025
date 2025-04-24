file = open('szyfrogram.txt','r')
linijki = file.readlines()
slownik = {}

for linijka in linijki:
    linijka = linijka.strip()
    for literka in linijka:
        literka = literka.strip()
        if literka not in slownik:
            slownik[literka] = 1
        else:
            slownik[literka] += 1

posortowane = dict(sorted(slownik.items(), key = lambda item: item[0]))
print(posortowane)

with open('zadanie 7_1.txt','w') as wynik:
    for klucz, wartosc in posortowane.items():
        wynik.write(f"{klucz} {wartosc}\n")
