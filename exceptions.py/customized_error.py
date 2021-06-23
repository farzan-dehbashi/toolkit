class ValueTooHighError(Exception):
    pass



def test_value(x):
    if x > 10:
        raise ValueTooHighError('Value is more than 10')

try:
    test_value(11)
except ValueTooHighError as error:
    print(error)