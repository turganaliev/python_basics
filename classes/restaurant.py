class Restaurant():
    def __init__(self, name, type):
        self.name = name
        self.type = type
    def describe_restaurant(self):
        long_name = self.name + '\n' + self.type
        return long_name.title()

class IceCreamStand(Restaurant):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.flavors = ['tasty', 'very tasty', 'best one']
    def show_flavors(self):
        print(self.flavors)
