file = open('dane4.txt','r')
linijki = file.readlines()

lista = []

for linijka in linijki:
    linijka = linijka.strip()
    lista.append(int(linijka))

max_liczba = 0
max_indeks = 0

for i in range(1,2023):
    par = 0
    aktualna_liczba = 0

    for j in range(i):
        if lista[i] > lista[j]:
            aktualna_liczba +=1
    if aktualna_liczba >= max_liczba:
        max_liczba = aktualna_liczba
        max_indeks = i

print(max_indeks+1)