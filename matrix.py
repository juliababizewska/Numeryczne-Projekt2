class Matrix:
    def __init__(self, n, m):
        self.matrix = [[0 for x in range(n)] for y in range(m)]

    def print(self):
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[0])):
                print(self.matrix[row][col], end=" ")
            print("")

    def get_row(self, index):
        return self.matrix[index]

    def get_column(self, index):
        column = []
        for row in range(len(self.matrix)):
            column.append(self.matrix[row][index])
        return column

    def get_element(self, row, column):
        return self.matrix[row][column]

    def set_element(self, row, column, element):
        self.matrix[row][column] = element

    def set_diagonal(self, index, element):
        n = len(self.matrix)  # Liczba wierszy macierzy
        m = len(self.matrix[0])  # Liczba kolumn macierzy

        if index == 0:
            # Ustawia elementy na głównej przekątnej
            for i in range(min(n, m)):
                self.set_element(i, i, element)
        elif index > 0:
            for i in range(min(n, m - index)):
                self.set_element(i, i + index, element)
        else:
            for i in range(min(n + index, m)):
                self.set_element(i - index, i, element)
