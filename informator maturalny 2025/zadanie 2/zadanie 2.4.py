plik = open('dane2_4.txt', 'r')
linijki = plik.readlines()

zbior = []

for linijka in linijki:

    linijka = linijka.strip()
    decyzja = ''
    lewa = 0
    prawa = 0

    for pojedyncza in linijka:

        if pojedyncza == '[':
            lewa += 1
        if pojedyncza == ']':
            prawa += 1
        if lewa == prawa:
            decyzja = 'tak'
        else:
            decyzja = 'nie'

    zbior.append((linijka, decyzja, lewa, prawa))

print(zbior)
