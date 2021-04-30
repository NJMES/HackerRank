# Link https://www.hackerrank.com/challenges/python-lists/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

if __name__ == '__main__':
    N = int(input())
    lst = []
    for x in range(0,N):
        rd =input().lower().replace('/',' ').split()
        cmd=rd[0]
        if cmd == 'insert':
            i = int(rd[1])
            e = int(rd[2])
            lst.insert(i,e)
        elif cmd == 'print':
            print(lst)
        elif cmd == 'remove':
            e = int(rd[1])
            lst.remove(e)
        elif cmd == 'append':
            e = int(rd[1])
            lst.append(e)
        elif cmd == 'sort':
            lst.sort()
        elif cmd == 'pop':
            lst.pop()
        elif cmd == 'reverse':
            lst.reverse()
        else:
            print('unsure')