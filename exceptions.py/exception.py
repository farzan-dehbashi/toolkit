# Errors and exceptions

# raise exception:
# raise Exception('This is a forced exception')

# assert exception:
# assert (5 == 3, '5 and 3 are not equal')

# try and catch:
try:
    a  = 5 / 0
except Exception as exception_message: # you can just have exception:
    print(exception_message)
else:
    print('OK')
finally:
    print('always this runs even if there is no exception')



