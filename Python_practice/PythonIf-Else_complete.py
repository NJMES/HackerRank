# link https://www.hackerrank.com/challenges/py-if-else/problem

#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if n%2!=0 or n%2==0 and n in range(6,21):   #Wierd  #range reads 6,but 21 is read as -1 pos, which is 20  
        print('Weird')
    elif n%2==0 and n in range(2,6) or n>20:    #Not Wierd  #range reads 2,but 6 is read as -1 pos, which is 5  
        print('Not Weird')
    else:
        print('its not weird or weird')