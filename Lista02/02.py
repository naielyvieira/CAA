def multiplicar_dividir_e_conquistar(A, B):
    n = len(A)


    if n == 1:
        return [[A[0][0] * B[0][0]]]


    a11, a12, a21, a22 = split_matrix(A)
    b11, b12, b21, b22 = split_matrix(B)


    m1 = multiplicar_dividir_e_conquistar(a11,subtrair_matrizes(b12, b22))
    m2 = multiplicar_dividir_e_conquistar(add_matrizes(a11, a12), b22)
    m3 = multiplicar_dividir_e_conquistar(add_matrizes(a21, a22), b11)
    m4 = multiplicar_dividir_e_conquistar(a22, subtrair_matrizes(b21, b11))
    m5 = multiplicar_dividir_e_conquistar(add_matrizes(a11, a22), add_matrizes(b11, b22))
    m6 = multiplicar_dividir_e_conquistar(subtrair_matrizes(a12, a22), add_matrizes(b21, b22))
    m7 = multiplicar_dividir_e_conquistar(subtrair_matrizes(a11, a21), add_matrizes(b11, b12))


    c11 = add_matrizes(subtrair_matrizes(add_matrizes(m5, m4), m2), m6)
    c12 = add_matrizes(m1, m2)
    c21 = add_matrizes(m3, m4)
    c22 = subtrair_matrizes(subtrair_matrizes(add_matrizes(m5, m1), m3), m7)


    result = combinar_matrizes(c11, c12, c21, c22)

    return result

def split_matrix(matrix):
    n = len(matrix)
    half_size = n // 2

    a11 = [row[:half_size] for row in matrix[:half_size]]
    a12 = [row[half_size:] for row in matrix[:half_size]]
    a21 = [row[:half_size] for row in matrix[half_size:]]
    a22 = [row[half_size:] for row in matrix[half_size:]]

    return a11, a12, a21, a22

def add_matrizes(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[i]))] for i in range(len(A))]

def subtrair_matrizes(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[i]))] for i in range(len(A))]

def combinar_matrizes(c11, c12, c21, c22):
    return c11 + c12 + c21 + c22

# Exemplo de uso:
A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
B = [[17, 18, 19, 20], [21, 22, 23, 24], [25, 26, 27, 28], [29, 30, 31, 32]]

resultado = multiplicar_dividir_e_conquistar(A, B)
print(resultado)
