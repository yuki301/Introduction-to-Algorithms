#伪代码中序列下标由1开始，本程序按照Python规范，列表下标由0开始。
def merge_sort(A,p,r):
    if p<r:
        q=(p+r)//2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)

def merge(A,p,q,r):
    n1=q-p+1
    n2=r-q
    L=[0]*(n1+1)
    R=[0]*(n2+1)
    for i in range(n1):
        L[i]=A[p+i]
    for j in range(n2):
        R[j]=A[q+j+1]
    L[n1]=None#此处为设置边界数。
    R[n2]=None
    i=0
    j=0
    for k in range(p,r+1):
        if L[i]==None:
            A[k]=R[j]
            j+=1
        elif R[j]==None:
            A[k]=L[i]
            i+=1
        else:
            if L[i]<=R[j]:
                A[k]=L[i]
                i+=1
            else:
                A[k]=R[j]
                j+=1
