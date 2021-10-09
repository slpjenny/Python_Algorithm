A,B = map(str,input().split())

# 상수는 숫자를 거꾸로 읽는다

# 더 큰 숫자 출력
print(max(int(A[::-1]),int(B[::-1])))
