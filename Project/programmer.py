"""
class Programmer
"""
from employee import Employee


class Programmer(Employee):

    def __init__(self, name, sal, email = None, tech_stack=None):
        super().__init__(name, sal)
        self.tech_stack = tech_stack if tech_stack is not None else None
        self.email = email if email is not None else None

    def __str__(self):
        return f"{super().__str__()}\nТехнологии: {self.tech_stack}"

    def work(self):
        return super().work()[:-1] + ' and start to coding.\n'

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
