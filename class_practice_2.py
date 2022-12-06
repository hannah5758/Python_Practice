class Family:
    def __init__(self):
        self.lastname = 'Lee'

    def print_lastname(self):
        print(f'last name is : {self.lastname}')


class Person(Family):
    def __init__(self):
        super(Person, self).__init__()
        self.firstname = 'Hannah'

    def print_firstname(self):
        print(f'first name is : {self.firstname}')
        

a = Family()
b = Person()

a.print_lastname()
b.print_firstname()
b.print_lastname()
