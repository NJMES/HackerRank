# link https://www.hackerrank.com/challenges/nested-list/problem?h_r=next-challenge&h_v=zen
# Nested List

'''
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
'''

if __name__ == '__main__':
    score = []
    for _ in range(0,int(input())):
        score.append([input(), float(input())])

    second_low = sorted(list(set([result for name, result in score])))[1]  
    #set to merge repeated scores. #make it a list. #sort it in ascending order. #second lowest is in index position [1].
    print('\n'.join([n for n,r in sorted(score) if r == second_low]))




''' old
if __name__ == '__main__':
    n = int(input())
    low=0
    ns=[]
    score_card = [[input(), float(input())] for x in range(n)]
    low = min(score_card, key=lambda x:x[1]) #sort list by (list, key=lambda // sort by nested list's position[1]# 2nd position ==value 
    ns=[score_card.remove(n,r) for n,r in score_card if r==low]
    print(score_card)
    print('\n'.join([name for name,result in sorted(score_card) if result==min(score_card, key=lambda y:y[1])[1]])) #'\n'--> print result in new Line
'''

''' 
old code
    score_card=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_card.append([name,score])
    sorted(score_card)
    scoremin= 0 
    for  i in range(len(score_card)):
        if score_card[i-1][1] < score_card[i][1]:
            scoremin=score_card[i-1][1]
    print(scoremin) 
'''