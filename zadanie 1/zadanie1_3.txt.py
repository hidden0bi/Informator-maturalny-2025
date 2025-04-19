plik = open('dane1_3.txt', 'r')
linijki = plik.readlines()
zbior = []
permutacje = []

for linijka in linijki:
    linijka = int(linijka)
    zbior.append(linijka)

    for i in range(1, len(zbior)):
        suma = sum(zbior[i : (len(zbior))]) #ładnie sobie idzie od elementu 0 do elementu n
        permutacje.append(suma)

maksymalne = max(permutacje)
print(maksymalne)