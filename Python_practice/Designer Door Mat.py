# https://www.hackerrank.com/challenges/designer-door-mat/problem?


nm = input().split()
n = int(nm[0])
m = int(nm[1])
#height
for i in range((n-1)/2):
    print ('.|.').center