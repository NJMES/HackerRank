# https://www.hackerrank.com/challenges/30-2d-arrays/problem

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    op = []

    for line in range(0, 4):  #read lines 1,2,3
        for ind in range(0, 4): #read char position 1,2,3
            hg = sum(arr[line][ind:ind+3]) + arr[line+1][ind+1] + sum(arr[line+2][ind:ind+3]) 
            # sum of (at line 0 - index from 0 to 0+3=3)
            # sum of (at line 0+1=1 - index at position = 0+1 =1)
            # sum of ( at line 0+2=2 - index from pos= 0 to 0+3=3 )  
            op.append(hg) # store all the sum in the op list.

    print(max(op)) #print the max number in output list.

    