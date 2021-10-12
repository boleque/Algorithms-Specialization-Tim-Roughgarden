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
def randomized_select(arr, order_statistic):
    pass
    