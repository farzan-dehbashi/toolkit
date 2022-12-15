class Product:
    def __init__(self, price= None) -> None:
        self.price = price

    @property
    def price(self):
        return self.__price

    @property.setter
    def price(self, value):
        if value <= 0:
            raise ValueError
        self.__price = value

    @property.getter
    def price(self):
        return self.__price


product = Product(10)
product.price = -1
print(product.get_price())
