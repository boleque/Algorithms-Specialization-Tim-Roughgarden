import random

# Trivial cases
# 1-th order statistic
def first_ordered_select(arr):
    first_ordered_elem = arr[0]
    for i in range(1, len(arr)):
        first_ordered_elem = min(first_ordered_elem, arr[i])
    return first_ordered_elem

# 2-th order statistic 
def second_ordered_select(arr):
    arrLen = len(arr)
    if arrLen == 1:
        return arr[0]
    elif arrLen == 2:
        return max(arr)

    if arr[1] < arr[0]:
        arr[0], arr[1] = arr[1], arr[0]
    first_ordered_elem = arr[0]
    second_ordered_elem = arr[1]

    for i in range(2, arrLen):
        second_ordered_elem = min(first_ordered_elem, arr[i])
        first_ordered_elem = min(first_ordered_elem, second_ordered_elem)

    return second_ordered_elem

# i-th order statistic
def r_select(arr, left_idx, right_idx, order_statistic):
    if left_idx == right_idx:
        return arr[left_idx]
    elif left_idx < right_idx:
        partition_idx = __partition(arr, left_idx, right_idx)
        k = partition_idx - left_idx + 1 # !!!
        if k == order_statistic:
            return arr[partition_idx]
        elif k > order_statistic:
            return r_select(arr, left_idx, partition_idx - 1, order_statistic)
        else:
            return r_select(arr, partition_idx + 1, right_idx, order_statistic - k)

def __partition(arr, left_idx, right_idx):
    pivot_idx = random.choice(xrange(left_idx, right_idx + 1))
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
#    r_select(A, 0, len(A) - 1, k)
