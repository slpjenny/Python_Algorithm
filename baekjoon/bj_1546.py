n = int(input())

#모든 점수 입력받기
score = list(map(int,input().split()))

#최고 점수 구하기
max = max(score)

newScore=[]
#점수 조작하기
for i in score:
    i=i/max*100
    newScore.append(i)

print(sum(newScore)/n)
