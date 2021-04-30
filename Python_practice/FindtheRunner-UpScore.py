# link :https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
#Find the Runner-Up Score!


if __name__ == '__main__':
    n = int(input())
    #map is read as an object/ set is to merge duplicate /list to make map/set object into list.
    arr = list(set(map(int, input().split())))      
    #print(arr)             #can print the new set/ list
    arr.remove(max(arr))    #remove the max element on the list to left with 2nd runnerup.
    print(max(arr))         #print the 2nd runner up.
