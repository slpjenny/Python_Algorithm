# test case number
T = int(input())

for i in range(T):
    # R-> 반복횟수 S-> 문자열
    R,S = input().split()

    # S는 문자열이기에 반복가능! 리스트로 바꿀 필요 없음
    for j in S:
        print(j*int(R),end='')
    print() 

    
    
