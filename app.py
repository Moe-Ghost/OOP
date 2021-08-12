"""
program context
"""

import traceback

from datetime import datetime

from employee import Employee
from recruiter import Recruiter
from programmer import Programmer
from candidate import Candidate
from vacancy import Vacancy


if __name__ == '__main__':
    try:
        recruiter = Recruiter("Nikita", 2)

        programmer1 = Programmer("Nataha", 4, 'py c++ c#')
        programmer2 = Programmer("Ihor", 3.4, 'py php js')

        candidate1 = Candidate('Hvan', 'c# php js', 'js', 'middle')
        candidate2 = Candidate('Huvan', 'py c++', 'c++', 'junior')
        candidate3 = Candidate('Ahvan', 'php py', 'py', 'senior')

        vacancy1 = Vacancy('developer', 'py', 'middle')
        vacancy2 = Vacancy('frontend', 'js', 'senior')

        emp = Employee('Chin-chin', 2, "1")

        candidate1.work()
        print(emp.info)
        print(Employee.chek_salary(emp.salary))

    except Exception as err:
        with open("logs.txt", 'a+') as f:
            f.write(f"{datetime.now()}\n\n")
            traceback.print_exc(file=f)
