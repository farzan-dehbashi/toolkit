class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{}{}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

dev_1 = Employee('Farzan', 'Dehbashi', 5000)
dev_2 = Employee('Mino', 'Shafti', 6000)

class Developer(Employee):
    raise_amount = 1.02 # if subclass has the same attribute as parent, the subclass atribute is used, else it traces back in the tree of parents to find the first.

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first,last,pay) #this uses the parent instructor to initiate the already implemented attributes
        self.prog_lang = prog_lang
developer1 = Developer('Saud', 'Faisal', 2000, 'python')
print(dev_1.fullname())
print(developer1.prog_lang)
print(isinstance(developer1, Employee))
print(issubclass(Developer,Employee))
