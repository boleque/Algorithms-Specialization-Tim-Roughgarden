#You are given as input an unsorted array of n distinct numbers, where n is a power of 2. 
#Give an algorithm that identifies the second-largest number in the array, and that uses at most n + logn - 2 comparisons.

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

#You are a given a unimodal array of n distinct elements, meaning that its entries are in 
#increasing order up until its maximum element, after which its elements are in decreasing order. 
#Give an algorithm to compute the maximum element that runs in O(log n) time.
# -*-  -*-

def max_in_unimodal_array(arr):
    arrLen = len(arr)
    if arrLen == 1:
        return arr[0]

    middle = arrLen // 2
    left_arr = arr[:middle]
    right_arr = arr[middle:]
    
    if left_arr[-1] < right_arr[0]:
        return max_in_unimodal_array(right_arr)
    else:
        return max_in_unimodal_array(left_arr)

#You are given a sorted (from smallest to largest) array A of n distinct integers which can be positive, 
#negative, or zero. You want to decide whether or not there is an index i such that A[i] = i. Design the 
#fastest algorithm that you can for solving this problem.

#You are given an n by n grid of distinct numbers. A number is a local minimum if it is smaller than all 
#of its neighbors. (A neighbor of a number is one immediately above, below, to the left, or the right.
#Most numbers have four neighbors; numbers on the side have three; the four corners have two.) Use the
#divide-and-conquer algorithm design paradigm to compute a local minimum with only O(n) 
#comparisons between pairs of numbers. (Note: since there are n2n^2n2 numbers in the input, you 
#cannot afford to look at all of them. Hint: Think about what types of recurrences would give you 
#the desired upper bound.)