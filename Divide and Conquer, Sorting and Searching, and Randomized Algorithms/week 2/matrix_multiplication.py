
# Brute force matrix multiplication algorithm - O(n^3)
def brute_force_matrix_multiplication(X, Y):
    matrixLen = len(X)
    res = [[0 for row in range(matrixLen)] for col in range(matrixLen)]
    for i in range(matrixLen):
        for j in range(matrixLen):
            for k in range(matrixLen):
                res[i][j] += X[i][k] * Y[k][j]
    return res


# Recursive matrix multiplication algorithm - O(n^3)
def recursive_matrix_multiplication(A, B):
    return __recursive_matrix_multiplication(A, B, 0, 0, 0, 0, len(A))

def __recursive_matrix_multiplication(A, B, rowA, colA, rowB, colB, size):    
    C = [[0 for row in range(size)] for col in range(size)]
    if size == 1:
        C[0][0] = A[rowA][colA] * B[rowB][colB];
    else:
        size //= 2
        # C11
        add_matrix(
            __recursive_matrix_multiplication(A, B, rowA, colA, rowB, colB, size), # A11 * B11
            __recursive_matrix_multiplication(A, B, rowA, colA+size, rowB+size, colB, size), # A12 * B21
            C,
            0,
            0
        )
        # C12
        add_matrix(
            __recursive_matrix_multiplication(A, B, rowA, colA, rowB, colB+size, size), # A11 * B12
            __recursive_matrix_multiplication(A, B, rowA, colA+size, rowB+size, colB+size, size), # A12 * B22
            C,
            0,
            size
        )
        # C21 
        add_matrix(
            __recursive_matrix_multiplication(A, B, rowA+size, colA, rowB, colB, size), # A21 * B11 
            __recursive_matrix_multiplication(A, B, rowA+size, colA+size, rowB+size, colB, size), # A22 * B21
            C,
            size,
            0
        )
        # C22
        add_matrix(
            __recursive_matrix_multiplication(A, B, rowA+size, colA, rowB, colB+size, size), # A21 * B12 
            __recursive_matrix_multiplication(A, B, rowA+size, colA+size, rowB+size, colB+size, size), # A22 * B22
            C,
            size,
            size
        )

    return C

def add_matrix(A, B, C, rowC, colC):
    lenA = len(A)
    for i in range(lenA):
        for j in range(lenA):
            C[i+rowC][j+colC] = A[i][j] + B[i][j]


# Strassen strassen's subcubic matrix multiplication algorithm - O(n^2)
# P1 = A(F-H)
# P2 = H(A+B)
# P3 = E(C+D)
# P4 = D(G-E)
# P5 = (A+D)(E+H)
# P6 = (B-D)(G+H)
# P7 = (A-C)(E+F)

# XY = (P5 + P4 - P2 + P6), (P1 + P2)
#      (P3 + P),(P1 + P5 - P3 - P7)


if __name__ == '__main__':
    
    X = [
        [5,6,5,6],
        [7,8,5,6],
        [7,8,5,6],
        [7,8,5,6],
    ]
    
    Y = [
        [1,2,1,2],
        [3,4,1,2],
        [1,2,1,2],
        [1,2,1,2],
    ]

    res1 = recursive_matrix_multiplication(X, Y)
    res2 = brute_force_matrix_multiplication(X, Y)
    
    print(">>> EQUAL={} rec={} brut={}".format(res1 == res2, res1, res2))