##################################################
## Author: Farzan Dehbashi
## Copyright: Copyright 2021,
## Date: ${DATE}
## Modified: ${DATE}
## Email: farzan.dehbashi95@gmail.com
## Status: {dev_status}
##################################################

def capitalize_words(arr = []):
    assert len(arr) >= 1, 'func <capitalize_words>: Non empty arr is expected!'
    my_list = []
    if len(arr) > 1:
        my_list.append(str(arr[len(arr)-1]).upper())

        return list(capitalize_words(arr[:len(arr)-1])) + my_list
    else:
        my_list.append(str(arr[0]).upper())
        return my_list
if __name__ == '__main__':
    print(capitalize_words(['i', 'am']))
