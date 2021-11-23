def solution(answers):
    #1번 수포자 : (1~5)반복
    #2번 수포자: 21 -> 23 -> 24-> 25
    #3번 수포자: (33 11 22 44 55) 반복

    #동점이면 모두 리턴
    #------------------------------
    answer = []
    
    supo1 = [1,2,3,4,5]
    supo2 = [2,1,2,3,2,4,2,5]
    supo3 = [3,3,1,1,2,2,4,4,5,5]
    
    supos = [supo1,supo2,supo3]

    gop = len(answers)//5 + 1
    
    for i in supos:
        i = i*gop  #수포자들의 찍는 답 개수 늘려놓음

    temp = []
    real_supos = []
    
    for k in supos: # k= supo1,2,3
        for j in range(0,len(answers)): # j= 0,1,2,3,4
            if answers[j] == k[j]:
                temp.append(k[j])
            
        k = len(temp)
        real_supos.append(k)

        #print(real_supos)  #real_supos 리스트 출력 

        temp.clear()


    m = max(real_supos)
    answer = [(i+1) for i,v in enumerate(real_supos) if v == m]
    print(answer)
    

solution([1,3,2,4,2])
