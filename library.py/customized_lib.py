print('Customized module is imported')

test = 'Test string'

def find_index(to_search, target):
    #finds the index of a value in a sequence
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1
