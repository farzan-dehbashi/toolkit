def func(a, b, c, d=4, *args, **kwargs): #default value of d (note that defualt arguments should be at the end)
    print(a, b, c, d)
    print(type(args))
    print(type(kwargs))

    for arg in args:
        print(arg)

    for key in kwargs:
        print(key, kwargs[key])

func(1, 2, 3, 7, 'arg1', 'arg2', 'arg3 can be int as well', age=10, city='Saudi')

def func2(a, b, c):
    print(a, b, c)
my_list = [1, 2, 3] # or have a tuple (1, 2, 3)
# or a dict {'a': 1, 'b':2, 'c':3} the keys should match the func2 keys and length should match and instead of *my_list, you should have **my_list
func2(*my_list)
