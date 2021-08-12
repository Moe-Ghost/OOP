"""
program context
"""
import sys
import traceback

from datetime import datetime
from datetime import date
from datetime import timedelta

from employee import Employee
from candidate import Candidate
from recruiter import Recruiter
from programmer import Programmer
from vacancy import Vacancy


if __name__ == '__main__':
    try:
        emp = Employee('Name(female)', 2, 'e')

        recruiter = Recruiter("Nikita", 2)

        programmer1 = Programmer("Nataha", 4, 'py c++ c#')
        programmer2 = Programmer("Ihor", 3.4, 'py php js')

        candidate1 = Candidate('Hvan', 'c# php js', 'js', 'middle')
        candidate2 = Candidate('Huvan', 'py c++', 'c++', 'junior')
        candidate3 = Candidate('Ahvan', 'php py', 'py', 'senior')

        vacancy1 = Vacancy('developer', 'py', 'middle')
        vacancy2 = Vacancy('frontend', 'js', 'senior')

        candidate1.work()

    except Exception as err:
        with open("logs.txt", 'a+') as f:
            f.write(f"-----\nDate: {datetime.now()}\nError type: {err.__class__.__name__}\n")
            traceback.print_exc(file=f)
