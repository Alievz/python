# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные
# (список списков) для формирования матрицы.

class Matrix:
    def __init__(self, list_1, list_2):
        self.matr = [list_1, list_2]
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matrix = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matrix[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))


    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))



my_matrix = Matrix([[40, 23, 12],
                    [-5, 9, 14],
                    [2, 0, 9]],
                   [[42, 1, 3],
                    [12, 12, 42],
                    [59, 38, 97]])

print(my_matrix.__add__())


