##################################################
## Author: Farzan Dehbashi
## Copyright: Copyright 2021,
## Date: ${DATE}
## Modified: ${DATE}
## Email: farzan.dehbashi95@gmail.com
## Status: {dev_status}
##################################################
obj = {
    'num': 1,
    'test': [],
    'data': {
        'val': 4,
        'info':{
            'isRight': True,
            'duck':2,
            'kin':
                {
                    'toyota': '2'
                }
        }
    }
}
def stringify(objects):
    sum =0
    for key in objects:
        if type(objects[key]) == dict:
            sum += stringify(objects[key])
        else:
            if type(objects[key]) == int or str(objects[key]).isdigit():
                sum += int(objects[key])

    return sum

if __name__ == '__main__':
    print(stringify(obj))
