def linear_search(A,v):
    for i in range(len(A)):
        if A[i]==v:
            return i
    return 'NIL'
