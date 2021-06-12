# decorators

def outer_function():
    message = ' sample message '

    def inner_function():
        print(message)
    return inner_function

my_function = outer_function()


my_function()
my_function()
my_function()
