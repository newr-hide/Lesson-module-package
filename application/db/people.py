

class Employees():
    def __init__(self,name,age,expiriens,salary):
        self.salary = salary
        self.expiriens = expiriens
        self.age = age
        self.name = name

    def get_employees(self):
        print(f'Найм сотрудника{self.name}  со ставкой {self.salary}')



employ_kuz = Employees('Кузькин','45','6','10000')



















