import math

from matrix import Matrix
from time import sleep


def invert_matrix(D):
    N = len(D.matrix)
    inverted_matrix = Matrix(N, N)
    for i in range(N):
        for j in range(N):
            if D.get_element(i, j) == 0:
                inverted_matrix.set_element(i, j, 0)
            else:
                inverted_matrix.set_element(i, j, 1 / D.get_element(i, j))
    return inverted_matrix


def invert_diagonal_matrix(D):
    N = len(D.matrix)
    inverted_matrix = Matrix(N, N)
    for i in range(N):
        diag_element = D.get_element(i, i)
        if diag_element == 0:
            raise ValueError("Diagonal matrix contains zero element, cannot invert.")
        inverted_matrix.set_element(i, i, 1 / diag_element)
    return inverted_matrix


# Calculate M = -(D)\(L+U)
def calculate_M_jacobi(D, L, U):
    # Invert the diagonal matrix D
    D_inv = invert_diagonal_matrix(D)
    # Calculate L + U
    N = len(L.matrix)
    LU_sum = Matrix(N, N)
    for i in range(N):
        for j in range(N):
            LU_sum.set_element(i, j, L.get_element(i, j) + U.get_element(i, j))
    # Calculate M = -D_inv * LU_sum
    M = Matrix(N, N)
    for i in range(N):
        for j in range(N):
            sum_val = 0
            for k in range(N):
                sum_val += D_inv.get_element(i, k) * LU_sum.get_element(k, j)
            M.set_element(i, j, -sum_val)
    return M


# Calculate bm = D\b
def calculate_bm_jacobi(D, b):
    # Invert the diagonal matrix D
    D_inv = invert_diagonal_matrix(D)
    # Calculate D_inv * b
    N = len(b.matrix[0])
    bm = Matrix(N, 1)
    for i in range(N):
        sum_val = D_inv.get_element(i, i) * b.get_element(0, i)
        bm.set_element(0, i, sum_val)
    return bm


def norm_euclidian(vector):
    """Oblicza normę euklidesową wektora."""
    sum_of_square = 0
    for v in range(len(vector.matrix[0])):
        value = vector.get_element(0, v)
        sum_of_square += value ** 2
    return sum_of_square ** 0.5


def solve_jacobi(A, b, bm, M, tolerance=1e-9):
    error = []
    N = len(M.matrix)
    x = Matrix(N, 1)
    # Inicjalizacja wektora x jako wektora zerowego
    for i in range(N):
        x.set_element(0, i, 1)

    iterations = 0
    while True:
        new_x = Matrix(N, 1)
        for i in range(N):
            new_value = bm.get_element(0, i)
            for j in range(N):
                M_ij = M.get_element(i, j)
                if M_ij != 0:
                    new_value += M_ij * x.get_element(0, j)
            new_x.set_element(0, i, new_value)
        # Oblicz residual i normę residuum
        residual = Matrix(N, 1)
        for i in range(N):
            res = b.get_element(0, i)
            for j in range(N):
                res -= A.get_element(i, j) * new_x.get_element(0, j)
            residual.set_element(0, i, res)
        # residual.print()
        err_norm = norm_euclidian(residual)
        print(err_norm)

        # Sprawdź warunek zbieżności
        if err_norm < tolerance:
            break

        # Aktualizuj wektor x
        # new_x.print()
        x = new_x
        iterations += 1


    return iterations, x


def solve_gauss_seidel(A, b, tolerance=1e-9):
    N = len(A.matrix)
    x = Matrix(N, 1)

    # Zainicjuj wektor x zerami
    for i in range(N):
        x.set_element(0, i, 0)

    iterations = 0
    while True:
        # Zmienna do przechowywania błędu iteracji
        err_norm = 0

        # Dla każdej wartości w wektorze x
        for i in range(N):
            sum_val = b.get_element(0, i)

            # Dodaj wartości z pozostałych elementów
            for j in range(N):
                if i != j:
                    sum_val -= A.get_element(i, j) * x.get_element(0, j)

            # Oblicz nową wartość x
            new_x_i = sum_val / A.get_element(i, i)

            # Oblicz błąd na podstawie różnicy pomiędzy nową wartością x a starą wartością x
            err_norm += (new_x_i - x.get_element(0, i)) ** 2

            # Zaktualizuj wartość x
            x.set_element(0, i, new_x_i)

        # Oblicz normę błędu
        err_norm = err_norm ** 0.5

        # Sprawdź warunek zbieżności
        if err_norm < tolerance:
            break

        iterations += 1

    return iterations, x
