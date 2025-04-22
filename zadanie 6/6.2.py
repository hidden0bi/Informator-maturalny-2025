file = open('dane6przyklad.txt','r')
linijki = file.readlines()
slownik = {p: [] for p in range(2,11)}

for p in range(2,11):
    licznik = 0
    for linijka in linijki:
        linijka = linijka.strip()
        p_minus = False
        wieksze_od = False
        for cyfra in linijka:
            cyfra = int(cyfra)
            if cyfra == p-1:
                p_minus = True
            if cyfra >= p:
                wieksze_od = True
                break # jezeli sie znajdzie, to wychodzi z petli, zeby nie zaliczac 10 razy tego samego, nie zmieni wyniku, to optymalizacja
        if p_minus and not wieksze_od:
            licznik += 1
            slownik[p].append(linijka)

#zwracanie najwiekszej wartosci
maksymalne = {}
for p, lista in slownik.items():
    if lista:
        maksymalne[p] = max(lista)
    print(p, licznik)
print(maksymalne)