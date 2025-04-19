plik = open('dane2_3.txt', 'r')
linijki = plik.readlines()

zbior = []


for linijka in linijki:

    linijka = linijka.strip()
    max_glebokosc = 0
    glebokosc = 0

    for pojedyncza in linijka:
        if pojedyncza == '[':
            glebokosc += 1
            if glebokosc > max_glebokosc:
                max_glebokosc = glebokosc
        elif pojedyncza == ']':
            glebokosc -= 1




    zbior.append((linijka, max_glebokosc))

print(zbior)

'''
file = open('dane2_3.txt','r')
in_file = file.readlines()

for line in in_file:
    current_depth = 0
    max_depth = 0
    line = line.strip()
    for char in line:
        current_depth += 1 if char == '[' else -1
        if char == '[' and current_depth > max_depth:
            max_depth = current_depth

print(max_depth)'''