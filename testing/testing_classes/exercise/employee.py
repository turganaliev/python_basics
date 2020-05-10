class Employee():
    def __init__(self, name, last_name, annual_salary):
        self.name = name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, increase=5000):
        raised = self.annual_salary + increase
        return raised
