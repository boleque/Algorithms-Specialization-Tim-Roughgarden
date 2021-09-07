# Example: (1,3,5,2,4,6)
# Inversions: (3,2), (5,2), (5,4)
# Usage https://en.wikipedia.org/wiki/Collaborative_filtering
# Max number of inversions: n*(n-1)/2

# Theory:
# left inversion i,j <= n/2
# right inversion i,j > n/2
# split inversion if i <= n/2 < j

from timeit import timeit

def sort_and_count(arr):
    arrLen = len(arr)
    if arrLen < 2:
        return arr, 0
    middle = arrLen // 2
    B, x = sort_and_count(arr[:middle])
    C, y = sort_and_count(arr[middle:])
    D, z = merge_and_count_split_inversion(B, C)

    return D, (x + y + z) 

def merge_and_count_split_inversion(B, C):
    D = []
    i = j = 0
    inv_count = 0

    while i < len(B) and j < len(C):
        
        if B[i] > C[j]:
            D.append(C[j])
            j += 1
            inv_count += (len(B)-i) 
        else:
            D.append(B[i])
            i += 1
        
    D.extend(B[i:])
    D.extend(C[j:])

    return D, inv_count

 
if __name__ == '__main__':
    input_array = None
    with open('IntegerArray.txt') as f:
        input_array = [int(x) for x in f.readlines()]
    begin = timeit()
    if input_array is not None:
        arr, inv_count = sort_and_count(input_array)
        print("Inversions number: ", inv_count) # 2407905288L
    end = timeit()
    print("Time: ", end - begin) # 0.0003689000000000114 