# link https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
# Day 8: Dictionaries and Maps

''' My solution but can't pass one of the test.
n = input()
phonebook={}
for i in range(int(n)):
    nmph = input().split()
    nm,ph = nmph[0],nmph[1]
    phonebook[nm]=ph

for i in range(int(n)):     #problem seems to be with my input. #has limits???
    try:
        sname = input()
    except:
        print('Not found')
    if sname in phonebook:
            print(sname+'='+phonebook[sname])
    else:
            print('Not found')
'''

#Model Answer
import sys 

# Read input and assemble Phone Book
n = int(input())
phoneBook = {}
for i in range(n):
    contact = input().split(' ')
    phoneBook[contact[0]] = contact[1]

# Process Queries
lines = sys.stdin.readlines()           #this is different from my input method
for i in lines:
    name = i.strip()
    if name in phoneBook:
        print(name + '=' + str( phoneBook[name] ))
    else:
        print('Not found')
