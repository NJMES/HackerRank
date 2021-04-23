#!/bin/python3
'''
Objective
In this challenge, we learn about conditional statements. Check out the Tutorial tab for learning materials and an instructional video.

Task
Given an integer, N, perform the following conditional actions:

    If N is odd, print Weird
    If N is even and in the inclusive range of 2 to 5, print Not Weird
    If N is even and in the inclusive range of 6 to 20, print Weird
    If N is even and greater than 20, print Not Weird

Complete the stub code provided in your editor to print whether or not is weird.

Input Format
A single line containing a positive integer, N

Constraints
. 1 <= n <= 100

Output Format
Print Weird if the number is weird; otherwise, print Not Weird.

Sample Input 0
3

Sample Output 0
Weird

Sample Input 1
24

Sample Output 1
Not Weird

Explanation
Sample Case 0:
is odd and odd numbers are weird, so we print Weird.

Sample Case 1:
and is even, so it is not weird. Thus, we print Not Weird.
'''

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    if N%2!=0 or N%2==0 and N in range(6,21):   #Wierd  #range reads 6,but 21 is read as -1 pos, which is 20  
        print('Weird')
    elif N%2==0 and N in range(2,6) or N>20:    #Not Wierd  #range reads 2,but 6 is read as -1 pos, which is 5  
        print('Not Weird')
    else:
        print('its not weird or weird')
