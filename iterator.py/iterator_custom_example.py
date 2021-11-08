# This makes an iteratable class that returns the next even number if the number does not exceed the max value.
class Even:
    def __init__(self, max):
        self.max = max
        self.next = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.next <= self.max:
            result = self.next
            self.next = self.next + 2
            return result
        else:
            raise StopIteration

if __name__ == '__main__':
    even_object = Even(10)
    iter_object = even_object.__iter__()
    while True:
        try:
            element = next(iter_object)
            print(element)
        except StopIteration:
            print('all elements are printed')
            break
