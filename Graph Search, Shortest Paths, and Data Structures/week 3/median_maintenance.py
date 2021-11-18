import heapq


def get_median(min_heap, max_heap):
    bigger, smaller = (min_heap, max_heap) if len(min_heap) > len(max_heap) else (max_heap, min_heap)
    if len(bigger) == len(smaller):
        return (abs(smaller[0]) + abs(bigger[0])) // 2
    else:
		return abs(bigger[0])

def get_data():
	with open("median.txt") as f:
		return (int(x.strip('\n')) for x in f.readlines())

def rebalance(min_heap, max_heap):
    bigger, smaller = (min_heap, max_heap) if len(min_heap) > len(max_heap) else (max_heap, min_heap)
    if len(bigger) - len(smaller) >= 2:
        heapq.heappush(smaller, -(heapq.heappop(bigger)))

def add_number(number, min_heap, max_heap):
    if not min_heap or number > min_heap[0]:
        heapq.heappush(min_heap, number)
    else:
        heapq.heappush(max_heap, -number)

def get_medians_sum(array):
    medians_sum = 0
    min_heap, max_heap = [], []
    for num in array:
        add_number(num, min_heap, max_heap)
        rebalance(min_heap, max_heap)
        medians_sum += get_median(min_heap, max_heap)
    return medians_sum

if __name__ == "__main__":
    input_array = get_data()
    median_sum = get_medians_sum(input_array)
    print(median_sum % 10000)
    # 1420