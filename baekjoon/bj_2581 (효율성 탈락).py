# M 이상 N 이하 자연수 중 소수인 것의 합/최솟값 출력

M = int(input())
N = int(input())

namugi = []
sosu = []

# 소수는 1과 자기자신만을 약수로 가지는 수(1제외) 
for i in range(M,N+1):
    for j in range(2,i+1):
        if i%j == 0:
            namugi.append(j)

    if len(namugi) == 1:
        sosu.append(i)

    namugi = []

# 소수가 해당범위 안에 없으면, -1 출력 
if len(sosu)==0:
    print(-1)

else:
    # 1) 소수의 합 출력
    print(sum(sosu))

    # 2) 최소 소수 출력
    print(min(sosu))



