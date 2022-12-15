class Product:
    def __init__(self, price= None) -> None:
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError
        self.__price = value

    @price.getter
    def price(self):
        return self.__price


product = Product(10)
product.price = -1
print(product.price)
