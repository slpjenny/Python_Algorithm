# C->테스트 케이스 수
C = int(input())

for i in range(C):
    scoreList = list(map(int,input().split()))

    # N -> 학생의 수
    N = scoreList[0]

    del scoreList[0]
    
    # 평균 구하기
    avg = sum(scoreList)/N

    # 평균 넘는 학생의 수
    avgN = 0
    for i in scoreList:
        if i > avg:
            avgN = avgN+1

    # 평균 넘는 하생들의 비율 구하기
    avgPortion = avgN/N * 100 

    print('%0.3f' %(avgPortion) + '%')
