def procedura(j, A):
    if j > 1:
        if A[j] < A[j-1]:
            v = A[j]
            A[j] = A[j-1]
            A[j-1] = v
            procedura(j-1, A)
    print(A,j)


#przykladowe dzialanie
A = [0,2,4,6,8,10,9,7,5,3,1] # cos musi byc na poczatku, bo pseudokod jest indeksowany od 1, a w pythonie od 0
j = 7
print(procedura(j,A))