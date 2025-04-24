def antypalindrom(s):
    """
        Funkcja sprawdza, czy napis s jest antypalindromem:
        dla każdego indeksu i w pierwszej połowie ciągu s,
        znak na pozycji i jest różny od znaku na pozycji (len(s)-1-i).

        UWAGA: W zadaniu podano indeksowanie od 1: s[i] ≠ s[n – i + 1],
        ale w Pythonie indeksy zaczynają się od 0, więc odpowiednikiem tego porównania
        jest: s[i] != s[len(s) - 1 - i]

        Dlaczego -1?
        Bo ostatni znak w Pythonie ma indeks len(s) - 1, a nie len(s), więc musimy go "przesunąć" o 1 w lewo.
        """
    warunek = True
    s = str(s)
    for i in range(len(s)//2):
        if s[i] == s[len(s)-i -1]:
            warunek = False
    return warunek

file = open('dane6przyklad.txt','r')
linijki = file.readlines()

for linijka in linijki:
    linijka = linijka.strip()

    if antypalindrom(linijka):
        print(f'{linijka}\n')
