"""
class Candidate
"""
from csv import DictReader

from exceptions import UnableToWorkException


class Candidate:
    def __init__(self, full_name, technologies, main_skill, main_skill_grade, email=None):
        self.full_name = full_name
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade
        self.email = email if email is not None else None

    def work(self):
        raise UnableToWorkException("I’m not hired yet, lol.")

    @classmethod
    def create_new_candidate(cls):
        with open("info.csv", "r") as f:
            reader = DictReader(f)

