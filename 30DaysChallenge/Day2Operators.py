#!/bin/python3
'''
Objective
In this challenge, you will work with arithmetic operators. Check out the Tutorial tab for learning materials and an instructional video.

Task
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost. Round the result to the nearest integer.

Example


A tip of 15% * 100 = 15, and the taxes are 8% * 100 = 8. Print the value

and return from the function.

Function Description
Complete the solve function in the editor below.

solve has the following parameters:

    int meal_cost: the cost of food before tip and tax
    int tip_percent: the tip percentage
    int tax_percent: the tax percentage

Returns The function returns nothing. Print the calculated value, rounded to the nearest integer.

Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result.

Input Format

There are
lines of numeric input:
The first line has a double, (the cost of the meal before tax and tip).
The second line has an integer, (the percentage of being added as tip).
The third line has an integer, (the percentage of

being added as tax).

Sample Input
12.00
20
8

Sample Output
15

'''

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip_percent = tip_percent * (meal_cost/100)
    tax_percent =(tax_percent/100) * tip_percent
    total = meal_cost + tip_percent + tax_percent
    return math.ceil(total)

if __name__ == '__main__':
    meal_cost = float(input()) #input field for HackerRank Input Variables.
    tip_percent = int(input())
    tax_percent = int(input())
    print(solve(meal_cost, tip_percent, tax_percent))

