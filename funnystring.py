import math  #import math for multiply within list --> math.prod(list)  

T = input('test cases:', )
for i in range(int(T)):

    s = [input('strings:', )]       #need to list the inputs strings in-order to reverse it.
    r = [reversed(s)]               #other way to reverse string --> r = s[::-1] 
    N = len(s)
    funny=list([int(1) if abs(ord(s[x])-ord(s[x-1]))==abs(ord(r[x])-ord(r[x-1])) else int(0) for x in range(1,N-1)])
    print('Not funny' if math.prod(funny)==0 else 'funny')

    '''
    funny=0
    for x in range(1,N-1) :
        #print(s[x],s[x-1])
        #print(r[x],r[x-1])
        #print(abs(ord(s[x])-ord(s[x-1])))
        #print(abs(ord(r[x])-ord(r[x-1])))
        
        if abs(ord(s[x])-ord(s[x-1])) == abs(ord(r[x])-ord(r[x-1])):
            funny+=1
        else:
            print('Not funny')
            break
    if funny>=1:
        print('funny')
    '''
