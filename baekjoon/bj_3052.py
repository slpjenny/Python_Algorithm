namugiL=[]


for i in range(10):
    
    n = int(input())
    namugi = n%42

    #나머지만 들어있는 리스트 생성
    namugiL.append(namugi)


#딕셔너리로 같은 나머지끼리 묶는다.
#나머지(키)의 종류 개를 출력한다.

namugiD={}

for i in namugiL:
    namugiD[i]=i

print(len(namugiD.keys()))
