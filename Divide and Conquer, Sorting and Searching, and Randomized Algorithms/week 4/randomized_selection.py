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
# i-th order statistic
def randomized_select(arr, left_idx, right_idx, order_statistic):
    if left_idx == right_idx:
        return arr[left_idx]
    elif left_idx < right_idx:
        partition_idx = __partition(arr, left_idx, right_idx)
        k = partition_idx - left_idx + 1
        if k == order_statistic:
            return arr[partition_idx]
        elif k > order_statistic:
            return randomized_select(arr, left_idx, partition_idx - 1, order_statistic)
        else:
            return randomized_select(arr, partition_idx + 1, right_idx, order_statistic - k)

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

if __name__ == '__main__':
    arr = [3, 8, 2, 5, 1, 4, 7, 6]
    res = randomized_select(arr, 0, len(arr)-1, 3)
    print('>> ordered statistic ', res)