A = int(input())
B = int(input())
C = int(input())

# 세 변수에 split을 이용해 한 번에 대입은 왜 안되는걸까?

mul = A*B*C

# 0~9가 몇 번 쓰였는지 1번째 줄 부터 출력해야 한다.

# 문자열 변환
sMul = str(mul)

print(sMul.count('0'))
print(sMul.count('1'))
print(sMul.count('2'))
print(sMul.count('3'))
print(sMul.count('4'))
print(sMul.count('5'))
print(sMul.count('6'))
print(sMul.count('7'))
print(sMul.count('8'))
print(sMul.count('9'))
