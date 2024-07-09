

class Calculate_salary():
    def __init__(self, employ,experience,age):
        self.age = age
        self.experience = experience
        self.emploee = employ


    def calc_salary(self):
        salary = self.experience * 10000
        print(f'Расчет зарплаты {self.emploee} {salary}')

mount_salary_kuz = Calculate_salary('Кузькин',6,'45')