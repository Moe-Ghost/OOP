from settings import date
from settings import timedelta
from models import Employee
from models import Recruiter
from models import Programmer
from models import Candidate
from models import Vacancy


if __name__ == '__main__':
    recruiter=Recruiter("Nikita", 2)

    programmer1=Programmer("Nataha", 4, 'py c++ c#')
    programmer2=Programmer("Ihor", 3.4, 'py php js')

    candidate1=Candidate('Hvan', 'c# php js', 'js', 'middle')
    candidate2=Candidate('Huvan', 'py c++', 'c++', 'junior')
    candidate3=Candidate('Ahvan', 'php py', 'py', 'senior')

    vacancy1=Vacancy('developer', 'py', 'middle')
    vacancy2=Vacancy('frontend', 'js', 'senior')