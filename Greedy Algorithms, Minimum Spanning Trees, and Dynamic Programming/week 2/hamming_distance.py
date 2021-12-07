
def distance(x, y):
    dist = 0
    z_xor = x ^ y
    while z_xor:
        dist += z_xor % 2
        z_xor >>= 1
    return dist

def test_distance():
    x = int('011001100101111110101101', 2)
    y = int('010001000101111110100101', 2)
    assert distance(x, y) == 3

if __name__ == '__main__':
    test_distance()