from django.db import models


# Create your models here.
class testMyClass:
    pass


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullInfo(self):
        return f'Employee\'s full information: {self.first} {self.last}. {self.email}'

emp1 = Employee('abc', 'xyz', 50000)

print(emp1.fullInfo())