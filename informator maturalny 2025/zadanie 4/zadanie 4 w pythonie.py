def SortW(n,lista):
    for i in range(2, len(lista)):
        v = lista[i] #zamiast A dalem lista, bo mi sie jebalo we lbie
        j = i
        while j > 1 and v < lista[j-1]:
            lista[j] = lista[j-1]
            j = j-1
        lista[j] = v
    return lista

#przykladowe wartosci zmiennych
n = 2
lista = [1,2,3,7,45,3,2,51]

print(SortW(n,lista))