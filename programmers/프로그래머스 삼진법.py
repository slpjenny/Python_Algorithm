def solution(n):
    answer = 0
    namugi = []
    samjin = 0
    
    while(n>0):
        namugi.append(n%3)  #0021
        n = n//3

    namugi.reverse()
    
    #0021 을 10진법으로 다시 바꾸기
    for i in namugi:
        answer = answer + 3**samjin * i
        samjin += 1
        
    return answer

