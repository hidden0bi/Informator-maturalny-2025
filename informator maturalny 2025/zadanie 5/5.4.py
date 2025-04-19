A = [0,2,4,6,8,10,9,7,5,3,1]
j=7

for j in range(len(A),1,-1):
    if j > 1:
        if A[j+1] < A[j]:
            v = A[j+1]
            A[j+1] = A[j]
            A[j] = v
        print(A, j)