newN=0
N = int(input())
originalN = int(N)
cycle=0


#입력한 수와 새로 만들어진 수가 같아질때까지 반복
while True:
    #자릿수 쪼개서 서로 더하기
    mok = N//10
    namugi = N%10

    hap = mok+namugi

    #오른쪽에 있는 수만 이어 붙이기 (나머지만!)
    N=int(str(namugi) + str(hap%10))
    
    #한 번 반복문 돌 때마다 횟수 세기 
    cycle=cycle+1

    if originalN == N : break

print(cycle)



    
