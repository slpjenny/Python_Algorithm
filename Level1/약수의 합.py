def solution(n):
    hap=0         #약수의 합을 담을 변수 
    
    for i in range(1,n+1):
        if n%i == 0:         #나눴을 때 나머지가 0 이면
            hap = hap +i     #합 변수에 계속 더한다
    
    return hap
