# M 이상 N 이하 자연수 중 소수인 것의 합/최솟값 출력

M = int(input())
N = int(input())

sosu=[]

num = set(range(2,N+1))  #일단 65까지 채우기 

# 소수는 1과 자기자신만을 약수로 가지는 수(1제외) 
for i in range(2,N+1):
    if i in num:  #해당 i의 배수들을 지워나간다. 에라토스테네스의 체 
        num -= set(range(2*i,N+1,i))  # 65이하의 소수들 

#2,3,5 ... 64,65

for j in num:
    if j in range(M,N+1):
        sosu.append(j)

        
# 소수가 해당범위 안에 없으면, -1 출력 
if len(sosu)==0:
    print(-1)
    
else:
    # 1) 소수의 합 출력
    print(sum(sosu))

    # 2) 최소 소수 출력
    print(min(sosu))

    
