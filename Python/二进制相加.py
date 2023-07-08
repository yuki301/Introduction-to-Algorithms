def binary_addition(A,B):
    n=len(A)
    carry=0
    C=[0]*(n+1)

    for i in range(n-1,-1,-1):
        sum=A[i]+B[i]+carry
        C[i+1]=sum%2

        if sum>=2:
            carry=1
        else:
            carry=0
    
    C[0]=carry

    return C
