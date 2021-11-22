import math

def power(base, exponent):
    if base > 0:
        if exponent == 1:
            return base
        elif exponent == 0:
            return 1
        elif exponent > 1:
            return power(base, exponent - 1) * base
        else:
            print('positive exponent is expected')
if __name__ == '__main__':
    if power(2, 8) == math.pow(2, 8):
        print(math.pow(2, 8))
    else:
        print('Test failed')