class Data:
    def __init__(self,date):
        Data.date = date

    @classmethod
    def date_to_date(cls):
        return [int(element) for element in cls.date.split(" ")]
    @staticmethod
    def validation_date(date):
        return False if date[0]>31 or date[1] > 12 or (date[1] == 2 and date[0]>28) else True

dat = Data("10 12 2004").date_to_date()
print(Data.validation_date(dat))

dat = Data("34 12 2004").date_to_date()
print(Data.validation_date(dat))

dat = Data("29 2 2004").date_to_date()
print(Data.validation_date(dat))




