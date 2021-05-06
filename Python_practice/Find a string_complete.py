#Find a string https://www.hackerrank.com/challenges/find-a-string/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def count_substring(string, sub_string):
    ssc=0
    ns=[ssc+1 for i in range(len(string)) if string[i:i+len(sub_string)] == sub_string] 
    #string[i:i+len(sub_string) is i is 1 the string will read till i + lenght of substring
    return sum(ns)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)