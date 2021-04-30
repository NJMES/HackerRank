# link https://www.hackerrank.com/challenges/finding-the-percentage/problem

# Finding the percentage
'''
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
'''

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        
    query_name = input()
    if query_name in student_marks:
        pr = '%.2f'% (sum(student_marks[query_name])/3)  #Able to sum, the value in a Dictionary
        # '%.2f'% format output into float with 2 decimal place
        print( pr)
        