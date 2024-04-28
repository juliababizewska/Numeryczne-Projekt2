from matrix import Matrix
class LinearSolver:
    def __init__(self, A, b):
        self.A = A
        self.b = b
        self.N = len(A.matrix)

    def diagonal(self):
        diag = Matrix(self.N, self.N)
        diag.set_diagonal(0, self.A.get_element(0, 0))
        return diag

    def upper_triangle(self):
        upper = Matrix(self.N, self.N)
        for i in range(0, self.N):
            for j in range(i + 1, self.N):
                upper.set_element(i, j, self.A.get_element(i, j))
        return upper

    def lower_triangle(self):
        lower = Matrix(self.N, self.N)
        for i in range(0, self.N):
            for j in range(i + 1, self.N):
                lower.set_element(self.N - 1 - i, self.N - 1 - j, self.A.get_element(self.N - 1 - i, self.N - 1 - j))
        return lower
