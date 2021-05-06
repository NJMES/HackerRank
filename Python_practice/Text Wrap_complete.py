#Text Wrap : 
# https://www.hackerrank.com/challenges/text-wrap/problem?

import textwrap

def wrap(string, max_width):
    ''' old code
    wwrap = textwrap.TextWrapper(width=max_width)       #set the Wrap width
    ns = wwrap.wrap(text=string)                        #wrap the string to the set width
    '''
    #ns = textwrap.wrap(text=string, width=max_width)   #new code merge width & string into one.

    return '\n'.join(textwrap.wrap(text=string, width=max_width) )  #new one line code

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)