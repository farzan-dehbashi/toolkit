import argparse

parser = argparse.ArgumentParser(description= 'configuration for the reader')
parser.add_argument('-f', '--frequency', type= float, metavar='', required= False, help='sets frequency of the reader')
parser.add_argument('-m', '--printmean', action= 'store_true',required=False, help='prints mean dataframe') #for no argument use store_true
args = parser.parse_args()

if __name__ == '__main__':
    if args.frequency:
        print("flag received")
    else:
        print("no flags found")
