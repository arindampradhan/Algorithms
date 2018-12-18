# counting sort O(nk)
# k is the max number of the array or the difference between max and min
# make sure k is less as higher k like 100000 will be very greater than O(nlogn)

def counting_sort(A):
    n = len(A)
    max_a = max(A)

    bucket = [0] * (max_a + 1)

    for i in range(n):
        val = A[i]
        bucket[val] = bucket[val] + 1

    for j in range(max_a):
        next_val = bucket[j + 1]
        curr_val = bucket[j]
        bucket[j + 1] = next_val + curr_val

    result = [0] * n
    for x in range(n):
        position = A[x]
        new_position = bucket[position]
        result[new_position-1] = position
        bucket[position] = bucket[position] - 1
    return result

print(counting_sort([1,4,1,2,7,5,2,89,1]))