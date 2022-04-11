
class Worker:
    def __init__(self,name,surname,position,wage,bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {}
        self.__income["wage"] = wage
        self.__income["bonus"] = bonus

class Position(Worker):
    def get_full_name(self):
        return f"Сотрудник: {self.name} {self.surname}"
    def get_total_income(self):
        return f"Должность: {self.position}\nОклад: {self._Worker__income['wage']}\nПремия: {self._Worker__income['bonus']}"

employee = Position("Дмитрий","Бачинин","Директор","200 тыс.","50 тыс.")
print(employee.get_full_name())
print("")
print(employee.get_total_income())

