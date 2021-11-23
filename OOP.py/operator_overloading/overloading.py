class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self):
        return f"({self.x},{self.y})"

    def __bool__(self):
        if self.x == 1:
            return True
        else:
            return False
    def __next__(self):
        return (1,1)

    def __call__(self, num):
        self.x = num
        print(self.x)
        return self.x

p1 = Point(3, 2)
p2 = Point(2, 3)
class Num_controller:
    def __init__(self, x_val): # this is x_val of the point num controller is controlling
        self.point = Point(x_val)

print(p1+p2)
print(bool(p1))
print(str(p1))
print(p1.__next__())
print(next(p1))
p1(2) # this is because we have overloaded call method, therefore, we act like an method to our object
num_manager = Num_controller(12)
num_manager.point(13)