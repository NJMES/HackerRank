# link https://www.hackerrank.com/challenges/python-lists/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    

    # for i in Range(x+1): for i is to index and run through range x+1 / range will stop before x, so we want it to read upto x so +1
    # j , k is the same loop process.
    # we know that value extracted from the 3 range 1,j,k can not be sum up equal to n, so i+j+k != n
    # we place the value we got from i,j,k into a nested list [i,j,k]

    ijk = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n ]
    print(ijk)
