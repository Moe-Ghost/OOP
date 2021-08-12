"""
class Recruiter
"""
from employee import Employee


class Recruiter(Employee):

    def work(self):
        return super().work()[:-1] + ' and start to hiring.\n'
