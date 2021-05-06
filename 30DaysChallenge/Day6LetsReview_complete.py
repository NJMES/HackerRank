'''
Objective
Today we will expand our knowledge of strings, combining it with what we have already learned about loops. 
Check out the Tutorial tab for learning materials and an instructional video.

Task
Given a string, 'S', of length 'N' that is indexed from '0' to 'N -1', print its even-indexed and 
odd-indexed characters as '2' space-separated strings on a single line 
(see the Sample below for more detail).

Note: () is considered to be an even index.

Example:
s = adbecf
Print 'abc' 'def'

Input Format:
The first line contains an integer,'T'(the number of test cases).
Each line 'i' of the 'T' subsequent lines contain a string, 'S'.

Constraints
    - 1 <= 'T' <= 10
    - 2 <= 'length of S' <=1000

Output Format
For each String 'S_j', (where 0 <= j <= T -1), print 'S_j''s even-indexed characters, 
followed by a space, followed by 'S_j''s odd-indexed characters.

Sample Input:
2
Hacker
Rank

Sample Output:
Hce akr
Rn ak

Explanation:

Test Case 0: "Hacker"
S[0] = "H"
S[1] = "a"
S[2] = "c"
S[3] = "k"
S[4] = "e"
S[5] = "r"

The even indices are '0','2'and '4', and the odd indices are '1','3' and '5'.We then print a single 
line of '2' space-separated strings; the first string contains the ordered characters from 'S''s 
even indices (Hce), and the second string contains the ordered characters from 'S''s odd indices (akr).

Test Case 1: "Rank"
S[0] = "R"
S[1] = "a"
S[2] = "n"
S[3] = "k"

The even indices are '0' and '2' , and the odd indices are '1'and '3' . 
We then print a single line of '2' space-separated strings; 
the first string contains the ordered characters from 'S''s even indices (Rn), 
and the second string contains the ordered characters from 'S''s odd indices (ak).
'''
'''  error output for other test case. problem with repeated char.
# Enter your code here. Read input from STDIN. Print output to STDOUT

tin = int(input())

for t in range(tin):
    s = str(input())
    se =''
    so = ''
    for i in s: 
        if s.index(i) % 2 == 0:
            se = se+i
        elif s.index(i) % 2 != 0:
            so = so+i
    print(se+' '+so)
'''
tin = int(input('No. of Strings', ))

for t in range(tin):
    s = str(input('Enter String:', ))        #string input
    se,so ='',''            #string even & string odd = blank
    
    for i in range(len(s)): #for i in range(lenght of string) i will run throught 0,1,2,3...stop before Range(length of s)
        if i % 2 == 0:      # if i is even 
            se = se+s[i]    # se + position i in the string s

        elif i % 2 != 0:    # if i is odd 
            so = so+s[i]    # so + position i in the string s

    print(se+' '+so)