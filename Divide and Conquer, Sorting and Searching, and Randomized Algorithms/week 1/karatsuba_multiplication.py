

def karatsuba_multiplication(x, y):

    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    nd2 = n/2

    ten_pow_nd2 = 10**nd2

    a = x / ten_pow_nd2
    b = x % ten_pow_nd2

    c = y / ten_pow_nd2
    d = y % ten_pow_nd2

    a_mul_c = karatsuba_multiplication(a, c)
    b_mul_d = karatsuba_multiplication(b, d)
    # reduce extra recursive calls to calculate a_mul_d and b_mul_c
    ad_plus_bc = karatsuba_multiplication(a + b, c + d) - a_mul_c - b_mul_d

    return (a_mul_c * ten_pow_nd2**2) + (ten_pow_nd2 * ad_plus_bc) + b_mul_d


if __name__ == '__main__':
    x = 3141592653589793238462643383279502884197169399375105820974944592
    y = 2718281828459045235360287471352662497757247093699959574966967627

    res = karatsuba_multiplication(x, y)
    # 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
    print('Result: ', res) 