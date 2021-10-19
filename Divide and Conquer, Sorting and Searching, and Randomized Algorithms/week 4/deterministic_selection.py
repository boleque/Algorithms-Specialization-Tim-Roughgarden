
# i-th order statistic
def d_select(arr, order_statistic):
    global indexByValue

    indexByValue = {v: i for i, v in enumerate(A)}   
    return _d_select(A, 0, len(A) - 1, order_statistic)

def _d_select(arr, left_idx, right_idx, order_statistic):
    arrLen = right_idx - left_idx
    if not arrLen:
        return arr[left_idx]
    elif arrLen > 0:
        pivot_idx = _median_of_median(arr, left_idx, right_idx, order_statistic)
        partition_idx = _partition(arr, pivot_idx, left_idx, right_idx)
        k = partition_idx - left_idx + 1
        if k == order_statistic:
            return arr[partition_idx]
        elif k > order_statistic:
            return _d_select(arr, left_idx, partition_idx - 1, order_statistic)
        else:
            return _d_select(arr, partition_idx + 1, right_idx, order_statistic - k)

def _partition(arr, left_idx, right_idx):
    #pivot_idx = #random.choice(xrange(left_idx, right_idx + 1))
    # important: swap elements to ensure pivot on the left most position
    arr[pivot_idx], arr[left_idx] = arr[left_idx], arr[pivot_idx]
    i = left_idx + 1
    pivot = arr[left_idx]
    for j in xrange(left_idx + 1, right_idx + 1):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i - 1], arr[left_idx] = arr[left_idx], arr[i - 1]    
    return i - 1

def _median_of_median(arr, left_idx, right_idx, order_statistic):
    arrLen = right_idx - left_idx
    if arrLen <= 5:
        return indexByValue[sorted(arr[left_idx:right_idx])[order_statistic]]
    C = []
    for i in range(left_idx, right_idx, 5):
        sample = arr[i:i + 5]
        sample.sort()
        sampleLen = len(sample)
        mid = sampleLen // 2
        C.append(sample[mid])
    return median_of_median(C, 0, arrLen//5, arrLen//10)
