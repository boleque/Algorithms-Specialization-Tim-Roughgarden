# quicksort impl

def quicksort(arr):
    pass

def _partition(arr, pivotIdx):
    p = arr[pivotIdx]
    i = pivotIdx + 1
    arrLen = len(arr)
    for j in range(i, arrLen):
        if arr[j] < p:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
        elif arr[j] > p:
            pass
    arr[pivotIdx], arr[i-1] = arr[i-1], arr[pivotIdx]
    return arr
    
if __name__ == '__main__':
    arr = [3, 1, 8, 2, 7, 3, 10, 6]   
    res = _partition(arr, 0)
    print('>> arr: ', res)