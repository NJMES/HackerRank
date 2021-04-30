# link https://www.hackerrank.com/challenges/python-lists/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split()) #map - makes splited inputs into int. [1, 2, 3...]
    t = tuple(integer_list)
    print(hash(t))