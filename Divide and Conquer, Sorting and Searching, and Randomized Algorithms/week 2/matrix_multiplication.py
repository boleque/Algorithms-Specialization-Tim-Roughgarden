# X = A B 
#     C D

# Y = E F
#     G H

# XY = (AE + BG), (AF + AH)
#      (CE + CG), (CF + DH)


# Brute force matrix multiplication algorithm - O(n^3)
def brute_force_matrix_multiplication(X, Y):
    matrixSize = len(X)
    res = [[0 for row in range(matrixSize)] for col in range(matrixSize)]
    for i in range(matrixSize):
        for j in range(matrixSize):
            sum = 0
            for k in range(matrixSize):
                sum += X[i][k] * Y[k][j]
            res[i][j] = sum
    return res


# Recursive matrix multiplication algorithm - O(n^3)
def recursive_matrix_multiplication(X, Y):
    if len(X) == 1:
        return X[0][0]*Y[0][0]
    
    A = None
    B = None
    C = None
    D = None

    E = None
    F = None
    G = None
    H = None
    
    ae = recursive_matrix_multiplication()
    bg = recursive_matrix_multiplication()
    ce = recursive_matrix_multiplication()
    cg = recursive_matrix_multiplication()
    af = recursive_matrix_multiplication()
    ah = recursive_matrix_multiplication()
    cf = recursive_matrix_multiplication()
    dh = recursive_matrix_multiplication()

    return

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
        [1,2,3], 
        [4,5,6], 
        [7,8,9]
    ]
    
    Y = [
        [9,3,1], 
        [4,8,3], 
        [5,6,1]
    ]