# divide and conquor
# recursive
# stable
# Not in-place - space complexity O(n) n + n/2 + n/4 + n/8 + ....1 = 2n
# O(nlog(n)) - time complexity
# T(n) = 2T(n/2) + cn
# k = nlogn

def merge(Arr, start, mid, end):
    temp = [0] * (end - start + 1)

    i = start # for left
    j = mid + 1 # for right

    k = 0 # for temp

    while i <= mid and j <= end:
        if Arr[i] <= Arr[j]:
            temp[k] = Arr[i]
            k = k + 1
            i = i + 1
        else:
            temp[k] = Arr[j]
            k = k + 1
            j = j + 1

    while i <= mid:
        temp[k] = Arr[i]
        k = k + 1
        i = i + 1
    while j <= end:
        temp[k] = Arr[j]
        k = k + 1
        j = j + 1


    for i in range(start, end+1):
        Arr[i] = temp[i - start]


def merge_sort(Arr, start, end):
    if start < end:
        mid = (start + end)/2
        merge_sort(Arr, start, mid)
        merge_sort(Arr, mid+1, end)
        merge(Arr, start, mid, end)
    return Arr

print(merge_sort([2,7,1,4,5,3,12,0], 0, 7))
