import unittest
from employee import Employee

class Test_Employee(unittest.TestCase):

    def test_give_default_raise(self):
        my_salary = Employee('Ivan', 'Durov', 10000)
        money = my_salary.give_raise()
        self.assertTrue(money)

    def test_give_custom_raise(self):
        my_salary = Employee('Ivan', 'Durov', 10000)
        money = my_salary.give_raise(10000)
        self.assertTrue(money)

unittest.main()
