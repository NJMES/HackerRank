# link https://www.hackerrank.com/challenges/30-recursion/problem

#!/bin/python3
'''
import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
'''

#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the factorial function below.
# factorial 5: 5! ---> 5 * 4 * 3 * 2 * 1  ---> 5 * 4!
# factorial 4: 4! ---> 4 * 3 * 2 * 1

def factorial(n):
    # Base case
    if n<=1:   
        #loop 4: 4 * 3 * 2 * 1
        return 1  #factiorial dealing with multiplication. so if 5*1=5,but if 5*0=0

    # Recursive case / keep looping.
    else:
        # if n = 4 ---> 4!
        # loop 1: 4 * factorial(4-1=3)
        # loop 2: 4 * 3 * factorial(3-1=2)
        # loop 3: 4 * 3 * 2 * factorial(2-1=1)
        return n * factorial(n-1) 

#summation example
# 4 + 3 + 2 + 1 + 0 ---> 4 summation[3 + 2 + 1]  
def summation(s):
    # Base case
    if s<=0:
        #loop4: s is now 0
        #return 3 + 2 + 1 + 0 = 6 (summation of s=3 is 6)
        return 0  #multi identity #why return 0? because 5+0=5, but if 5x0=0

    # Recursive case / keep looping.
    else:
        #if we start with s=3
        #loop 1: 3 + summation(3-1=2)
        #loop 2: 3 + 2 + summation(2-1=1)
        #loop 3: 3 + 2 + 1 + summation(1-1=0)
        return s + summation(s-1) #calling the function summation created the loop

#5^3 = 5 * 5 * 5
#5^3 --> 5 * 5^2 --> 5 * 5 * 5^1  --> 5 * 5 * 5 * 5^0 --> 5 * 5 * 5 * 5 * 1
def exponentiation(n,p):  #example: exponentiation(5,3) 5 never changes, but 3 will be iterate by recursion
    # Base case
    if p<=0:        
        return 1    #multi indentity
    
    #recursive case // looping
    else:
        # 5 * exponentiation(5, 2)
        # 5 * 5 * exponentiation(5, 1)
        # 5 * 5 * 5 * exponentiation(5, 0)
        # 5 * 5 * 5 * 1
        return n * exponentiation(n, p-1)
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    result = factorial(n)
    fptr.write(str(result) + '\n')
    fptr.close()


