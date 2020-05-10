import unittest
from employee import Employee

class Test_Employee(unittest.TestCase):

    def setUp(self):
        self.my_salary = Employee('Leonardo', 'da Vinci', 100)

    def test_give_default_raise(self):
        money = self.my_salary.give_raise()
        self.assertTrue(money)

    def test_give_custom_raise(self):
        money = self.my_salary.give_raise(1)
        self.assertTrue(money)

unittest.main()
