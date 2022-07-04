from application.salary import calculate_salary
from application.people import get_employees
import datetime


if __name__ == '__main__':
    get_employees()
    calculate_salary()
    print(datetime.datetime.now())
