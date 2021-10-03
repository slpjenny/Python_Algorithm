N = []

for i in range(9):
    N.append(int(input()))

choidae = max(N)

#최대값 출력
print(choidae)
#최대값이 몇 번째 수인지 출력
print(N.index(choidae)+1)
