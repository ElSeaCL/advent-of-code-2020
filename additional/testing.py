# testing.py

from timer import Timer
from day1 import *

L1 = [1721, 979, 366, 299, 675, 1456]

def main():
    '''Print the time that takes to run the function suma2020'''
    t = Timer()
    t.start()
    producto = suma2020(L1)
    t.stop()

    print(producto)

if __name__ == "__main__":
    main()

