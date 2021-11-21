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


if __name__ == "__main__":
    data = get_data()
    get_two_sum_count(data)