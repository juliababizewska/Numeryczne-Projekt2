from matrix import Matrix
from math import sin
from LinearSolver import LinearSolver
import other_functions
import time

indeks = 193206
#N = 906
N = 10
A = Matrix(N,N)
e = 2
f = 3
b = Matrix(N,1) #jedno wierszowa macierz, więc wektor, u know

a1 = 5 + e
a2 = -1
a3 = -1

A.set_diagonal(0,a1)
A.set_diagonal(1,a2)
A.set_diagonal(-1,a2)
A.set_diagonal(-2,a3)
A.set_diagonal(2,a3)


for i in range(N):
    pom = sin(i*(f+1))
    b.set_element(0, i,  pom)
#b.print()

solver = LinearSolver(A, b)
D = solver.diagonal() #macierz diagonalna
U = solver.upper_triangle() #macierz górna trójkatna
L = solver.lower_triangle() #maciesz dolna trójkątna


#D * M = -(L+U)


# M = other_functions.calculate_M_jacobi(D, L, U)
# bm = other_functions.calculate_bm_jacobi(D, b)
# start_time = time.perf_counter()
# iterations, x_solution = other_functions.solve_jacobi(A, b, bm, M,  tolerance=1e-9)
# end_time = time.perf_counter()
# execution_time = end_time - start_time

# x_solution.print()
# print("Iterations: ", iterations)
# print("Time: ", execution_time)

start_time = time.perf_counter()
iterations, x_solution = other_functions.solve_gauss_seidel(A, b,tolerance=1e-9)
end_time = time.perf_counter()
execution_time = end_time - start_time
#x_solution.print()
print("Iterations: ", iterations)
print("Time: ", execution_time)