from django.db import models


# Create your models here.
class testMyClass:
    pass


class Employee:
    total_employee = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first + '.' + last + '@company.com'
        Employee.total_employee += 1

    # More for developer
    def __repr__(self):
        return f'{self.first}, {self.last}, {self.pay}, {self.email}'

    # More for End user
    def __str__(self):
        return f'{self.email}'

    # Over writing default add
    def __add__(self, other):
        return self.pay + int(other.pay)

    # Overwriting default len
    def __len__(self):
        return len(self.fullInfo())

    # When using @property decorator, must remove the original variable in class
    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, given):
        first, last = given.split(' ')
        self.first = first
        self.last = last

    def fullInfo(self):
        return f'Employee\'s full information: {self.email}. Pay: {self.pay}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)



    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # Can be used as alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, language):
        # Ask the parent class to handle below
        super().__init__(first, last, pay)
        self.language = language

        # Below is the same super().__init__()
        # Employee.__init__(self, first, last, pay)


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None, ):
        super().__init__(first, last, pay)

        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp_to_manage(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp_to_manage(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def show_emp_managing(self):
        for emp in self.employees:
            print(f'-->{emp.fullInfo()}')
