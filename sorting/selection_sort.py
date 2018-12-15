def selection_sort(A, n):
    for i in range(0, n - 1): # 0 ..... n-2 as n - 2 will be the largest
        i_min = i
        for j in range(i + 1, n):
            if A[j] < A[i_min]:
                i_min = j
        A[i], A[i_min]  = A[i_min], A[i]
    return A

print(selection_sort([2,7,1,4,5,3], 6))