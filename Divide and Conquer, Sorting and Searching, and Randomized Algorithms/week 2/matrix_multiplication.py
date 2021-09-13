# -*- coding: utf8 -*-

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
        add_matrices(
            __recursive_matrix_multiplication(A, B, rowA, colA, rowB, colB, size), # A11 * B11
            __recursive_matrix_multiplication(A, B, rowA, colA+size, rowB+size, colB, size), # A12 * B21
            C,
            0,
            0
        )
        # C12
        add_matrices(
            __recursive_matrix_multiplication(A, B, rowA, colA, rowB, colB+size, size), # A11 * B12
            __recursive_matrix_multiplication(A, B, rowA, colA+size, rowB+size, colB+size, size), # A12 * B22
            C,
            0,
            size
        )
        # C21 
        add_matrices(
            __recursive_matrix_multiplication(A, B, rowA+size, colA, rowB, colB, size), # A21 * B11 
            __recursive_matrix_multiplication(A, B, rowA+size, colA+size, rowB+size, colB, size), # A22 * B21
            C,
            size,
            0
        )
        # C22
        add_matrices(
            __recursive_matrix_multiplication(A, B, rowA+size, colA, rowB, colB+size, size), # A21 * B12 
            __recursive_matrix_multiplication(A, B, rowA+size, colA+size, rowB+size, colB+size, size), # A22 * B22
            C,
            size,
            size
        )

    return C

def add_matrices(A, B, C, rowC, colC):
    lenA = len(A)
    for i in range(lenA):
        for j in range(lenA):
            C[i+rowC][j+colC] = A[i][j] + B[i][j]

def sub_matrices(A, B, C, rowC, colC):
    lenA = len(A)
    for i in range(lenA):
        for j in range(lenA):
            C[i+rowC][j+colC] = A[i][j] - B[i][j]

# Strassen strassen's subcubic matrix multiplication algorithm - O(n^2)
# P1 = A11*(B12−B22)
# P2 = (A11+A12)*B22
# P3 = (A21+A22)*B11
# P4 = A22*(B21−B11)
# P5 = (A11+A22)*(B11+B22)
# P6 = (A12−A22)*(B21+B22)
# P7 = (A11−A21)*(B11+B12)

# XY = (P5 + P4 - P2 + P6), (P1 + P2)
#      (P3 + P4),           (P5 + P1 - P3 - P7)

def strassen_matrix_multiplication(A, B):
    size = len(A)
    if size == 1:
        return [[A[0][0]*B[0][0]]]

    def add_matrices(a, b):
        size = len(a)
        res = [[0 for row in range(size)] for col in range(size)]
        for i in range(size):
            for j in range(size):
                res[i][j] = a[i][j] + b[i][j]
        return res
    
    def sub_matrices(a, b):
        size = len(a)
        res = [[0 for row in range(size)] for col in range(size)]
        for i in range(size):
            for j in range(size):
                res[i][j] = a[i][j] - b[i][j]
        return res
    
    half = size // 2
    A11 = [A[i][:half] for i in range(half)]
    A12 = [A[i][half:] for i in range(half)]
    A21 = [A[i][:half] for i in range(half, size)]
    A22 = [A[i][half:] for i in range(half, size)]
    B11 = [B[i][:half] for i in range(half)]
    B12 = [B[i][half:] for i in range(half)]
    B21 = [B[i][:half] for i in range(half, size)]
    B22 = [B[i][half:] for i in range(half, size)]

    P1 = strassen_matrix_multiplication(A11, sub_matrices(B12, B22)) #A11*(B12−B22)
    P2 = strassen_matrix_multiplication(add_matrices(A11, A12), B22) #(A11+A12)*B22
    P3 = strassen_matrix_multiplication(add_matrices(A21, A22), B11) #(A21+A22)*B11
    P4 = strassen_matrix_multiplication(A22, sub_matrices(B21, B11)) #A22*(B21−B11)
    P5 = strassen_matrix_multiplication(add_matrices(A11, A22), add_matrices(B11,B22)) # (A11+A22)*(B11+B22)
    P6 = strassen_matrix_multiplication(sub_matrices(A12, A22), add_matrices(B21,B22)) # (A12−A22)*(B21+B22)
    P7 = strassen_matrix_multiplication(sub_matrices(A11, A21), add_matrices(B11,B12)) # (A11−A21)*(B11+B12)
    
    C11 = add_matrices(sub_matrices(add_matrices(P5, P4), P2), P6)   # P5 + P4 - P2 + P6
    C12 = add_matrices(P1, P2) # P1 + P2
    C21 = add_matrices(P3, P4) # P3 + P4
    C22 = sub_matrices(sub_matrices(add_matrices(P5, P1), P3), P7) # P5 + P1 - P3 - P7

    C = []
    for v1, v2 in zip(C11, C12):
            C.append(v1 + v2)
    for v1, v2 in zip(C21, C22):
        C.append(v1 + v2)
    return C
            
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

    res1 = strassen_matrix_multiplication(X, Y)
    res2 = brute_force_matrix_multiplication(X, Y)
    
    print(">>> EQUAL={} rec={} brut={}".format(res1 == res2, res1, res2))