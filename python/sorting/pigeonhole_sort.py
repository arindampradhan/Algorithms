# works for integer based array
# suitable for sorting lists of elements where the number of elements and the number of possible key values are approximately the same.
# O(n + k) time complexity
# O(n) space complexity

def pigeonhole_sort(A):
    min_a = min(A)
    max_a = max(A)

    pigeonhole_size = max_a - min_a + 1

    holes = [0] * pigeonhole_size

    for x in A:
        holes[x - min_a] += 1
    
    i = 0
    for count in range(pigeonhole_size):
        while holes[count] > 0:
            holes[count] -= 1
            A[i] = count + min_a
            i = i + 1
    return A

        
print(pigeonhole_sort([5,2,8,4,6,1,88]))