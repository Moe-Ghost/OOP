from settings import date
from settings import timedelta


class Employee:
    def __init__(self, name, sal):
        self.name = name
        self.salary = sal

    def work(self):
        return 'I come to office.'

    def chek_salary(self):
        now = date.today()
        start = date(now.year, now.month, 1)
        weekend = [5, 6]
        days = (now - start).days + 2
        day_count = 0
        for day in range(days):
            if(start + timedelta(day)).weekday() not in weekend:
                day_count += 1
        return self.salary * day_count

    def __str__(self):
        return f"Должность: {self.__class__.__name__} \nИмя: {self.name}"

    def __eq__(self, other):
        return self.salary == other.salary

    def __ne__(self, other):
        return self.salary != other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def __le__(self, other):
        return self.salary <= other.salary


class Recruiter(Employee):

    def work(self):
        return super().work()[:-1]+ ' and start to hiring.\n'


class Programmer(Employee):

    def __init__(self, name, sal, tech_stack = None):
        super().__init__(name, sal)
        if tech_stack != None:
            self.tech_stack = tech_stack

    def __str__(self):
        return f"{super().__str__()}\nТехнологии: {self.tech_stack}"

    def work(self):
        return super().work()[:-1]+ ' and start to coding.\n'

    def __eq__(self, other):
        return len(self.tech_stack) == len(other.tech_stack)

    def __ne__(self, other):
        return len(self.tech_stack) != len(other.tech_stack)

    def __lt__(self, other):
        return len(self.tech_stack) < len(other.tech_stack)

    def __gt__(self, other):
        return len(self.tech_stack) > len(other.tech_stack)

    def __ge__(self, other):
        return len(self.tech_stack) >= len(other.tech_stack)

    def __le__(self, other):
        return len(self.tech_stack) <= len(other.tech_stack)

    def __add__(self, other):
        stack = (set(self.tech_stack.split() + other.tech_stack.split()))
        return self.__class__("sup", 100, " ".join(stack))

class Candidate:
    def __init__(self, full_name, email = None, technologies, main_skill, main_skill_grade):
        self.full_name = full_name
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade


class Vacancy:
    def __init__(self, title, main_skill, main_skill_level):
        self.title = title
        self. main_skill = main_skill
        self.main_skill_level = main_skill_level