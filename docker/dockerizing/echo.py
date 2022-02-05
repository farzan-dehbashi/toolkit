import numpy as np

def main():
    print('Hi') 
    print(f'arr = {np.array([1,2,3,4])}')
    while True:
        s = input('Tell me about yourself: ')
        print(f'{s} me too!')
        if s == 'finish':
            return 0

if __name__ == '__main__':
    main()