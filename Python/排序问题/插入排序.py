def insertion_sort(A):
    for j in range(2,len(A)):
        key=A[j]
        i=j-1
        while i>0 and A[i]>key:#此处A[i]与key比较使用大于号，表明此排序为升序
            A[i+1]=A[i]
            i-=1
        A[i+1]=key


