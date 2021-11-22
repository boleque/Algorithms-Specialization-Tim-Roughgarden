import time
from collections import deque


def get_data():
    with open('2sum.txt') as f:
        return set([int(x.strip('\n')) for x in f.readlines()])

def get_two_sum_count(data):
    count = 0
    targets = range(-10000, 10000)
    for trg in targets:
        for val in data:
            if (trg - val) in data and trg - val != val:
                count += 1
                break
    return count

def _get_two_sum_count_rec(targets, data):
    global counter

    dataLen = len(data)
    if dataLen == 1:
        return data
    
    pivot = dataLen // 2
    left_part, right_part = divide_data(pivot, data)

    v1 = _get_two_sum_count_rec(targets, left_part)
    v2 = _get_two_sum_count_rec(targets, right_part)

    unionSet = v1.union(v2)
    targetsLen = len(targets)
    while targetsLen:
        target = targets.popleft()

        for v in unionSet:
            if (target - v) in unionSet and target - v != v:
                counter += 1
                break
        else:
            targets.append(target)

        targetsLen -= 1
    return unionSet

def divide_data(pivot, data):
    left_most = set()
    right_most = set()
    set_it = iter(data)
    it = 0

    while it < pivot:
        left_most.add(next(set_it))
        it += 1

    while it < len(data):
        right_most.add(next(set_it))
        it += 1

    return left_most, right_most

def get_two_sum_count_rec(data):
    global counter
    
    targets = deque(range(-10000, 10000))
    counter = 0

    _get_two_sum_count_rec(targets, data)
    return counter

if __name__ == "__main__":
    data = get_data()

    start_rec_ts = time.time()
    c1 = get_two_sum_count_rec(data)
    end_rec_ts = time.time()
    print('recursive scanning took: ', end_rec_ts - start_rec_ts)

    start_linear_ts = time.time()
    c2 = get_two_sum_count(data)
    end_linear_ts = time.time()
    print('linear scanning took: ', end_linear_ts - start_linear_ts)

    print('c1={} c2={}'.format(c1, c2))