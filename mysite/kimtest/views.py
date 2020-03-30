from django.shortcuts import render
from .models import Employee

# Create your views here.
def kimtest(request):

    emp1 = Employee('Abc', 'Xyz', 100)
    emp2 = Employee('KKK', 'XXX', 111)
    emp1.apply_raise()
    emp1.apply_raise()

    emp1.raise_amount = 1.11
    print(f'Employee.raise_amount: {Employee.raise_amount}')
    print(f'emp1.raise_amount: {emp1.raise_amount}')
    print(f'Total Employees: {Employee.total_employee}')
    print(emp1.__dict__)

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



