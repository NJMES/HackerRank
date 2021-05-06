# link https://www.hackerrank.com/challenges/30-binary-numbers/problem

# day 10 Binary Numbers.

#!/bin/python3

'''
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
'''
import math
import os
import random
import re
import sys

if __name__ == '__main__': 

    #method 01 using bin()
    n= int(input())
    r = max(bin(n)[2:].split('0')).count('1')
    print (r)