# 할머니가 외운 단어
word = str(input())

# 알파벳 24개를 덩어리로 나누어 놓는다.
alp = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

# 걸리는 최소시간
time = 0

for i in word:
    for j in alp:
        if i in j:
            time = time + alp.index(j)+3

print(time)
