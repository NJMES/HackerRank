
#!/bin/python3
# Day 7: Arrays
# link: https://www.hackerrank.com/challenges/python-lists/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    arr.reverse()   #reverse the list
    o=''            #empty string for output
    for i in range(n):      #run through seq 0 to n - limiter n.
        o = o + str(arr[i])+ ' '    #string o add the content in arr's position sequence
    print(o)            #print string o