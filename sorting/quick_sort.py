# Divide and conquer
# In place
# O(nlogn) - best
# O(n^2) - worst

def partition(A, start, end):
    pivot = A[end]
    pIndex = start
    for i in range(start, end - 1):
        if A[i] <= pivot:
            A[i], A[pIndex] = A[pIndex], A[i]
            pIndex = pIndex + 1
    A[pIndex], A[end] = A[end], A[pIndex]
    return pIndex

# better alternative
# def random_partition(A, start, end):
#    pass  

def quick_sort(A, start, end):
    if start < end:
        partitionIndex = partition(A, start, end)
        quick_sort(A, start,partitionIndex - 1)
        quick_sort(A,partitionIndex+1, end)
    return A

print(quick_sort([2,7,1,4,5,3,12,0], 0, 7))