def selection_sort(A,n):
    for i in range(n-1):
        smallest=A[i]
        for j in range(i+1,n):
            if A[j]<A[smallest]:
                smallest=j
        A[i],A[smallest]=A[smallest],A[i]