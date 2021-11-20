N = int(input())

namugi = []
sosu = []

nlist = list(map(int,input().split()))


for j in nlist:

    #1이 소수일 경우를 생각하지 않음.
    for k in range(2,j+1):
        if j%k==0:
            namugi.append(k)

    if len(namugi)==1:
        sosu.append(j)

    namugi = []

print(len(sosu))
            
