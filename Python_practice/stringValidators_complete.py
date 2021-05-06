# https://www.hackerrank.com/challenges/string-validators/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

if __name__ == '__main__':
    s = input()
    
    halnum =[ 1 if x.isalnum()==True else 0 for x in s ]
    print('True' if sum(halnum)>=1 else 'False')

    halpha =[ 1 if x.isalpha()==True else 0 for x in s ]
    print('True' if sum(halpha)>=1 else 'False')

    hdigit =[ 1 if x.isdigit()==True else 0 for x in s ]
    print('True' if sum(hdigit)>=1 else 'False')

    hlower =[ 1 if x.islower()==True else 0 for x in s ]
    print('True' if sum(hlower)>=1 else 'False')

    hupper =[ 1 if x.isupper()==True else 0 for x in s ]
    print('True' if sum(hupper)>=1 else 'False')