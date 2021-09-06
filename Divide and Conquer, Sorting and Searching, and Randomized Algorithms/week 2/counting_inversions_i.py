# Example: (1,3,5,2,4,6)
# Inversions: (3,2), (5,2), (5,4)
# Usage https://en.wikipedia.org/wiki/Collaborative_filtering
# Max number of inversions: n*(n-1)/2

# Theory:
# left inversion i,j <= n/2
# right inversion i,j > n/2
# split inversion if i <= n/2 < j

def count(arr):
    arrLen = len(arr)
    if arrLen == 1:
        return 0
    middle = arrLen // 2

    x = count(arr[:middle])
    y = count(arr[middle:])
    z = count_split_inversion(arr) 

    return x + y + z

def count_split_inversion(arr):
    middle = len(arr) // 2
    inv_count = 0
    for i in range(middle):
        for j in range(middle, len(arr)):

            if arr[i] > arr[j]:
                inv_count += 1

    return inv_count