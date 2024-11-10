# Non-recursive, worst - O(n^2) best - O(n), not - inplace (non constant time)

def insertion_sort(A, n):
    for i in range(1 , n):
        value = A[i]
        hole = i
        while hole > 0 and A[hole - 1] > value:
            A[hole] = A[hole - 1]
            hole = hole - 1
        A[hole] = value
    return A

print(insertion_sort([2,7,1,4,5,3], 6))