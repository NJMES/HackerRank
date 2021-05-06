# https://www.hackerrank.com/challenges/python-mutations/problem?h_r=next-challenge&h_v=zen

'''
Input (stdin)
    abracadabra
    5 k

Expected Output
    abrackdabra
'''

def mutate_string(string, position, character):
    ns = string[:position]+str(character)+string[position+1:]
    return ns

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)