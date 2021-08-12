"""
class Employee
"""
from datetime import date
from datetime import timedelta


class Employee:
    def __init__(self, name, sal, email=None):
        self.name = name
        self.salary = sal
        if email is not None:
            self.email = email
            self.validate_email()
            self.save_email()

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

    def work(self):
        return 'I come to office.'

    @staticmethod
    def check_salary(salary):
        now = date.today()
        start = date(now.year, now.month, 1)
        weekend = [5, 6]
        days = (now - start).days + 1
        day_count = 0
        for day in range(days):
            if(start + timedelta(day)).weekday() not in weekend:
                day_count += 1
        return salary * day_count

    def save_email(self):
        with open('emails.txt', 'a+') as f:
            f.write(f'{self.email}\n')

    def validate_email(self):
        with open("emails.txt", 'r') as f:
            if self.email in f:
                raise ValueError('sh*t')

    @property
    def info(self):
        i = ["Position: "+self.__class__.__name__,
             "Name: "+self.name,
             "Worked days: "+str(Employee.check_salary(self.salary)//self.salary)]
        return "\n".join(i)
