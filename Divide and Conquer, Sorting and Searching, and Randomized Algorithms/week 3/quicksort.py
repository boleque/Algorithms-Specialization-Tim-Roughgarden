
def quick_sort(arr, left_idx, right_idx, mode):
    if left_idx < right_idx:
        partition_idx = __partition(arr, left_idx, right_idx, mode)
        quick_sort(arr, left_idx, partition_idx - 1, mode)
        quick_sort(arr, partition_idx + 1, right_idx, mode)

def __partition(arr, left_idx, right_idx, mode):
    global comparisons

    if mode == 'first':
        pivot_idx = left_idx
    elif mode == 'last':
        pivot_idx = right_idx
    elif mode == 'mean':
        pivot_idx = median_of_three(arr, left_idx, right_idx)
    #else:
    #    pivot_idx = random

    # important: swap elements to ensure pivot on the left most position
    arr[pivot_idx], arr[left_idx] = arr[left_idx], arr[pivot_idx]
    i = left_idx + 1
    pivot = arr[left_idx]
    for j in range(left_idx + 1, right_idx + 1):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i - 1], arr[left_idx] = arr[left_idx], arr[i - 1]
    # important: number of comparisons are equal to distance between right and left boundaries
    comparisons += right_idx - left_idx
    return i - 1

def median_of_three(arr, left_idx, right_idx):
    mid_idx = left_idx + (right_idx - left_idx) // 2
    li = [(arr[left_idx], left_idx), (arr[mid_idx], mid_idx), (arr[right_idx], right_idx)]
    li.sort(key=lambda x: x[0])
    return li[1][1]

if __name__ == "__main__":
    array = []
    with open("QuickSort.txt") as f:
        array = [int(x) for x in f.readlines()]
    arrayLen = len(array)

    comparisons = 0    
    quick_sort(list(array), 0, arrayLen - 1, 'first')
    print("\n>> Left most pivot; Number of comparisons: {}".format(comparisons)) # 162085

    comparisons = 0    
    quick_sort(list(array), 0, arrayLen - 1, 'last')
    print("\n>> Right most pivot; Number of comparisons: {}".format(comparisons)) # 164123

    comparisons = 0    
    quick_sort(list(array), 0, arrayLen - 1, 'mean')
    print("\n>> Mean pivot; Number of comparisons: {}".format(comparisons)) # 138382