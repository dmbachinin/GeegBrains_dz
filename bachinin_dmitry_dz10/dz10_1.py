class Matrix:
    def __init__(self, matrix_mass):
        self.matrix = matrix_mass

    def __str__(self):
        res = ""
        for line in self.matrix:
            for element in line:
                res += f"{element} "
            else:
                res = res[:-1]
                res += "\n"
        return res[:-1]

    def __add__(self, mat):
        matrix_res = []
        for num_line, line in enumerate(self.matrix):
            matrix_res.append(line[:])
            for num_element, element in enumerate(line):
                try:
                    matrix_res[num_line][num_element] += mat.matrix[num_line][num_element]
                except IndexError:
                    if num_element == 0:
                        matrix_res[num_line] = []
                        break
                    else:
                        matrix_res[num_line][num_element] = None

        for line in reversed(matrix_res):
            if not line:
                matrix_res.pop()
            else:
                for element in reversed(line):
                    if not element:
                        line.pop()
        return Matrix(matrix_res)


print("Вывод массивов")
mat1 = Matrix([[1, 2, 5, 6, 7, 8], [9, 10, 11, 12]])
print(mat1,"\n")

mat2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(mat2,"\n")

print("Сложение массивов")
mat3 = mat2 + mat1
print(mat3,"\n")

mat4 = mat1 + mat2
print(mat4,"\n")

print("Повторный вывод начальных массивов")
print(mat2,"\n")

print(mat1,"\n")
