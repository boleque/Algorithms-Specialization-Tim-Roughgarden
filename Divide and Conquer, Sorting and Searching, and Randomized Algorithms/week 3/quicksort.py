def quickSort(arr, leftBoundary, rightBoundary):
    if leftBoundary < rightBoundary:
        partitionBoundary = __partition(arr, leftBoundary, rightBoundary)
        quickSort(arr, leftBoundary, partitionBoundary-1)
        quickSort(arr, partitionBoundary+1, rightBoundary)

def __partition(arr, leftBoundary, rightBoundary):
    i = leftBoundary - 1
    pivot = arr[rightBoundary]
    for j in range(leftBoundary, rightBoundary):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]           
    arr[i+1], arr[rightBoundary] = arr[rightBoundary], arr[i+1]
    return i + 1

#if __name__ == '__main__':
#    arr1 = [8,2,3,5,1,4,7,6]
#    arr2 = [3,2,8,5,1,4,7,6]
#
#    quickSort(arr1, 0, len(arr1)-1)  
#    quickSort(arr2, 0, len(arr2)-1)  
#    print('>> Res: ', arr1, arr2)
   
#class PIVOT_MODE:
#	EXTREME_LEFT = 0
#	EXTREME_RIGHT = 1
#	MEAN_OF_THREE = 2
    
#def get_mean_of_three(a, left, right):
#    mid = (left + right) // 2
#    li = [(a[left], left), (a[mid], mid), (a[right], right)]
#    li.sort()
#    return li[1][1]

#if __name__ == "__main__":
#	
#	with open("QuckSortInput.txt") as f:
#		input = [int(x) for x in f.readlines()]
#	#print("input ", len(input))
#	comparisons = 0
#	quick_sort(input, 0, len(input) - 1)
#	res = "RESULT: {}".format(comparisons)
#	print(res)
#
## left 162085 right 164123 mean 138382