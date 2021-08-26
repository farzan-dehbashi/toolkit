class sample_class:
    # class methods
    # it changes the class itself instead of the instance of the class
    attribute = 'default value'
    @classmethod
    def class_method(cls, atr_amount):
        cls.attribute = atr_amount
    # regular methods
    # they pass self as the instance to the method
    def regular_method(self):
        print('regular method')
    # static methods
    # dont pass anything. just have some rational connection with the class
    @staticmethod
    def static_method(number): #return if the number is even
        if number%2 == 0:
            return 'is even'
        return 'is odd'
sample_class.class_method('new value') # it changes all of the attribute values of all instance of that class at once

instance1 = sample_class()
print(instance1.attribute)
print(sample_class.static_method(3))