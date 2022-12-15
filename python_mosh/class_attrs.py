class Point:
    default_color = "red"

    @classmethod
    def zero(cls):
        return cls(0,0)

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

point = Point(1,2)
point = Point.zero()
print(point.x)
