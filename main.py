import datetime
from tqdm import tqdm

from application.db.people import Employees, employ_kuz
from application.salary import Calculate_salary, mount_salary_kuz


def hour_x():
    current_datetime = datetime.datetime.now(tz=None)
    formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print("Текущие дата и время:", formatted_date)


Calculate_salary.calc_salary(mount_salary_kuz)
Employees.get_employees(employ_kuz)



if __name__ == '__main__':
    for i in tqdm(range(1000000)):
        pass
    print(f"Запустился main")
    hour_x()