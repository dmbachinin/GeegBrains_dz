class Cell:

    def __init__(self, cell_count):
        self.size = cell_count

    def __add__(self, cell_2):
        return Cell(self.size + cell_2.size)

    def __str__(self):
        return f"{self.size}"

    def __sub__(self, cell_2):
        if self.size - cell_2.size < 0:
            print("Вычитание этих клеток невозможно!")
        else:
            return Cell(self.size - cell_2.size)

    def __mul__(self, cell_2):
        return Cell(self.size * cell_2.size)

    def __truediv__(self, cell_2):
        return Cell((self.size + cell_2.size) // 2)

    def make_order(self, count_val):
        result_str = ""
        count = 0
        for _ in range(cell_1.size):
            result_str += "*"
            count += 1
            if count == count_val:
                result_str += "\n"
                count = 0

        return result_str
    
cell_1 = Cell(17)
cell_2 = Cell(13)

print("Сложение клеток")
cell_3 = cell_1 + cell_2
print(cell_3,"\n")

print("Вычитание клеток")
cell_4 = cell_1 - cell_2
print(cell_4,"\n")

cell_5 = cell_2 - cell_1
print(cell_5,"\n")

print("Умножение клеток")
cell_6 = cell_1 * cell_2
print(cell_6,"\n")

print("Деление клеток")
cell_7 = cell_1 / cell_2
print(cell_7,"\n")

print("make_order:")
print(cell_1.make_order(7))
