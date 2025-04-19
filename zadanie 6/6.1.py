file = open('dane6przyklad.txt','r')
linijki = file.readlines()
p_minimalne = 0

for linijka in linijki:
    linjika = linijka.strip()
    for cyfra in linijka:
        cyfra = int(cyfra.strip())
        for p in range(2,10):
            if cyfra == p:
                p_minimalne +=1

                break




print(p_minimalne)