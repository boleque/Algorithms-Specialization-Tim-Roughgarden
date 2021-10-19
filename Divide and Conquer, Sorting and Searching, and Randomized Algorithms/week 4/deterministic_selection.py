def median_of_median(arr, left_idx, right_idx, order_statistic):
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

def d_select(arr, left_idx, right_idx, order_statistic):
    arrLen = right_idx - left_idx
    if not arrLen:
        return arr[left_idx]
    elif arrLen > 0:
        pivot_idx = median_of_median(arr, left_idx, right_idx, order_statistic)
        partition_idx = __partition(arr, pivot_idx, left_idx, right_idx)
        k = partition_idx - left_idx + 1
        if k == order_statistic:
            return arr[partition_idx]
        elif k > order_statistic:
            return d_select(arr, left_idx, partition_idx - 1, order_statistic)
        else:
            return d_select(arr, partition_idx + 1, right_idx, order_statistic - k)

def __partition(arr, pivot_idx, left_idx, right_idx):
    #pivot_idx = left_idx #random.choice(xrange(left_idx, right_idx + 1))
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

#if __name__ == '__main__':
#    A = [39, 20, 28, 52, 17, 26, 36, 62, 91, 16, 87, 10, 88, 77, 63, 80, 47, 60, 23, 43, 67, 14, 74, 6, 59, 65, 24, 64, 34, 53, 93, 85, 38, \
#        48, 41, 8, 31, 5, 83, 45, 78, 81, 32, 66, 54, 98, 49, 4, 12, 94, 44, 72, 25, 96, 82, 1, 19, 3, 58, 15, 95, 42, 76, 90, 50, 30, 55, 57, \
#        61, 13, 71, 29, 21, 70, 33, 89, 68, 27, 40, 75, 35, 51, 37, 22, 11, 18, 46, 86, 73, 97, 2, 92, 99, 9, 79, 7, 84, 69, 56]
#    k = 10
#    global indexByValue
#    indexByValue = {v: i for i, v in enumerate(A)}
#    d_select(A, 0, len(A) - 1, k)
