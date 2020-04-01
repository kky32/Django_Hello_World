from django.shortcuts import render
from .models import Employee, Developer, Manager
import datetime

# Create your views here.
def kimtest(request):

    emp1 = Employee('Abc', 'Xyz', 100)

    # They are the same
    Employee.raise_amount = 1.00
    Employee.set_raise_amt(1.00)

    # example of @classmethod from_string()
    emp_str1 = 'KKK-YYY-10000'
    emp_str2 = 'AAA-BBB-22000'
    emp_str3 = 'YYY-ZZZ-33000'

    emp2 = Employee.from_string(emp_str3)
    print(f' emp2.pay: {emp2.pay}')

    # emp1.raise_amount = 1.11
    print(f' Employee.raise_amount: {Employee.raise_amount}')
    print(f' emp1.raise_amount: {emp1.raise_amount}')
    print(f' Total Employees: {Employee.total_employee}')
    print(emp1.__dict__)

    # test static method is_workday
    my_date = datetime.date(2020, 3, 30)
    # print(f' {my_date.strftime("%Y-%B-%d")}')
    print(Employee.is_workday(my_date))

    dev1 = Developer('Kim', 'Zzz', 100, 'Python')
    dev1.apply_raise()
    print(f' {dev1.__dict__} \n')
    # print(help(dev1))

    manager1 = Manager('Big', 'Manager', 101, [emp1])
    manager1.add_emp_to_manage(dev1)
    manager1.add_emp_to_manage(manager1)
    manager1.show_emp_managing() # prints 3 employees
    print(f'{manager1.__dict__}')

    manager1.remove_emp_to_manage(manager1)
    manager1.show_emp_managing() # prints 2 employees
    print(f'{manager1.__dict__}')

    # Check if instance of a class
    print(isinstance(manager1, Manager))

    # Check if subclass
    print(issubclass(Manager, Employee))

    print(manager1)
    print(repr(manager1))
    print(str(manager1))

    # They are the same
    print(1+2)
    print(int.__add__(1, 2))

    # They are the same
    print('a' + 'b')
    print(str.__add__('a', 'b'))

    print(emp1 + emp2)

    # They are the same
    print(len('test'))
    print('test'.__len__())

    # They are the same
    print(len(manager1))
    print(manager1.__len__())

    # @property
    manager1.first = 'Small'
    print(manager1.getEmail)

    context = {
        'test': emp1,

        'kim' : emp1.fullInfo(),
        'kim2': Employee.fullInfo(emp1),

        'example1': emp1.raise_amount,
        'example2': Employee.raise_amount,

        'dict': emp1.__dict__,
        'dict1': Employee.__dict__,
        'dict2': emp1.__dict__.items(),
        'dict3': emp1.__dict__.keys(),
        'dict4': emp1.__dict__.values(),

    }
    return render(request, 'kimtest/test.html', context)



