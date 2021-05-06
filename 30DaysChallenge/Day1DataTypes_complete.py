'''
Objective
Today, we're discussing data types. Check out the Tutorial tab for learning materials and an instructional video!

Task
Complete the code in the editor below. The variables
, , and

are already declared and initialized for you. You must:

    Declare 

variables: one of type int, one of type double, and one of type String.
Read
lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your
variables.
Use the
operator to perform the following operations:

    Print the sum of 

plus your int variable on a new line.
Print the sum of
plus your double variable to a scale of one decimal place on a new line.
Concatenate

        with the string you read as input and print the result on a new line. 

Note: If you are using a language that doesn't support using

for string concatenation (e.g.: C), you can just print one variable immediately following the other on the same line. The string provided in your editor must be printed first, immediately followed by the string you read as input.

Input Format

The first line contains an integer that you must sum with
.
The second line contains a double that you must sum with .
The third line contains a string that you must concatenate with

.

Output Format

Print the sum of both integers on the first line, the sum of both doubles (scaled to
decimal place) on the second line, and then the two concatenated strings on the third line.
'''
i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
i1=input()      #input allows HackerRank TestCase Variables.
d1=input()      
s1=input()
# Read and save an integer, double, and String to your variables.
i1=i+int(i1)
d1=d+float(d1)
s1=s+str(s1)
# Print the sum of both integer variables on a new line.
print(i1)
# Print the sum of the double variables on a new line.
print(d1)
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s1)

