#You are given as input an unsorted array of n distinct numbers, where n is a power of 2. 
#Give an algorithm that identifies the second-largest number in the array, and that uses at most n +logn - 2 comparisons.

# little bit similar https://leetcode.com/problems/third-maximum-number/


def second_largest_number(arr):
    res = [None, None]
    _second_largest_number(arr, res)
    _first_max, second_max = res
    return second_max

def _second_largest_number(arr, res):
    arrLen = len(arr)
    if arrLen == 1:
        return arr[0]
    
    middle = arrLen // 2
    v1 = _second_largest_number(arr[:middle], res)
    v2 = _second_largest_number(arr[middle:], res)
    
    maxVal = max(v1, v2)
    minVal = min(v1, v2)

    res[0] = max(res[0], maxVal)
    res[1] = max(res[1], minVal)

    return maxVal