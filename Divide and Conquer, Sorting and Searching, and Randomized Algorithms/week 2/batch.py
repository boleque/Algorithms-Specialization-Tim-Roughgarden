#You are given as input an unsorted array of n distinct numbers, where n is a power of 2. 
#Give an algorithm that identifies the second-largest number in the array, and that uses at most n + logn - 2 comparisons.

# little bit similar https://leetcode.com/problems/third-maximum-number/
import sys


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
def find_index_value_equal(arr):
    valueToIndexMap = {v: i for i, v in enumerate(arr)}
    print('>> valueToIndexMap ', valueToIndexMap)
    return _find_index_value_equal(arr, valueToIndexMap)

def _find_index_value_equal(arr, valueToIndexMap):
    arrLen = len(arr)
    if not arrLen:
        return False

    middle = arrLen // 2
    value = arr[middle]
    index = valueToIndexMap[arr[middle]]
    if value == index:
        return index
    elif value > index:
        return _find_index_value_equal(arr[:middle], valueToIndexMap)
    else:
        return _find_index_value_equal(arr[middle:], valueToIndexMap)
    
#You are given an n by n grid of distinct numbers. A number is a local minimum if it is smaller than all 
#of its neighbors. (A neighbor of a number is one immediately above, below, to the left, or the right.
#Most numbers have four neighbors; numbers on the side have three; the four corners have two.) Use the
#divide-and-conquer algorithm design paradigm to compute a local minimum with only O(n) 
#comparisons between pairs of numbers. (Note: since there are n2n^2n2 numbers in the input, you 
#cannot afford to look at all of them. Hint: Think about what types of recurrences would give you 
#the desired upper bound.)


def findLocalMinimun(arr):
	arrLen = len(arr)
	topRowIdx = 0
	bottomRowIdx = arrLen - 1
	while topRowIdx <= bottomRowIdx:
		midRowIdx = topRowIdx + (bottomRowIdx - topRowIdx) // 2
		minColIdx = findMinColIndex(arr[midRowIdx])
		minRowIdx = findMinRowIndexNeighborhood(arr, midRowIdx, minColIdx)
		if minRowIdx == midRowIdx:
			return arr[minRowIdx][minColIdx]
		elif minRowIdx < midRowIdx:
			bottomRowIdx = midRowIdx - 1
		else:
			topRowIdx = midRowIdx + 1
		

def findMinRowIndexNeighborhood(arr, middleRow, minColIndex):
	arrLen = len(arr)
	valueBelow, valueAbove = sys.maxint, sys.maxint
	valueMiddle = arr[middleRow][minColIndex]
	if middleRow-1 >= 0:
		valueBelow = arr[middleRow-1][minColIndex]

	if middleRow+1 <= arrLen:
		valueAbove = arr[middleRow+1][minColIndex]
	
	minValue = min(valueMiddle, valueBelow, valueAbove)
	if minValue == valueMiddle:
		return middleRow
	elif minValue == valueBelow:
		return middleRow-1
	else:
		return middleRow+1

def findMinColIndex(arr):
	minRow = 0
	minElement = sys.maxint
	for idx, val in enumerate(arr):
		if val < minElement:
			minElement = val
			minRow = idx
	return minRow



if __name__ == '__main__':
	arr1 = [
		[30, 19, 18, 40, 16, 45, 13],
		[43, 14, 15, 12, 25, 34, 17],
		[24, 1, 32, 33, 31, 36, 11],
		[44, 6, 48, 46, 39, 27, 8],
		[29, 20, 49, 26, 28, 22, 7],
		[38, 4, 47, 5, 10, 23, 3],
		[42, 41, 37, 2, 9, 35, 21],
	]

	arr2 = [
		[17, 16, 32, 15, 23, 36],
		[20, 3, 18, 35, 11, 9],
		[26, 5, 8, 30, 13, 22],
		[10, 31, 2, 1, 7, 14],
		[28, 12, 6, 24, 25, 34],
		[29, 21, 27, 19, 4, 33],
	]

	res = findLocalMinimun(arr2)
	print('>> local minimum is: ', res)





