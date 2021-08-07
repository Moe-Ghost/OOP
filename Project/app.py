"""
program context
"""
import sys
import traceback
from datetime import datetime
from datetime import date
from datetime import timedelta

from models import Employee
from models import Recruiter
from models import Programmer
from models import Candidate
from models import Vacancy


if __name__ == '__main__':
    try:
        # recruiter = Recruiter("Nikita", 2)

        # programmer1 = Programmer("Nataha", 4, 'py c++ c#')
        # programmer2 = Programmer("Ihor", 3.4, 'py php js')

        # candidate1 = Candidate('Hvan', 'c# php js', 'js', 'middle')
        # candidate2 = Candidate('Huvan', 'py c++', 'c++', 'junior')
        # candidate3 = Candidate('Ahvan', 'php py', 'py', 'senior')

        # vacancy1 = Vacancy('developer', 'py', 'middle')
        # vacancy2 = Vacancy('frontend', 'js', 'senior')

        emp = Employee('v', 10, "2@gmail.com")

        candidate1 = Candidate('Hvan', 'c# php js', 'js', 'middle')
        candidate1.work()

    except Exception as err:
        with open("logs.txt", 'a+') as f:
            f.write(f"{datetime.now()}\n")
            traceback.print_exc(file=f)
