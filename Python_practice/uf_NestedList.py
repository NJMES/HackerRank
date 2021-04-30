# link https://www.hackerrank.com/challenges/nested-list/problem?h_r=next-challenge&h_v=zen
# Nested List

'''
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
'''
if __name__ == '__main__':
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