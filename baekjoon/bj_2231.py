N = int(input())
count = 0

for i in range(1,N):
    if i+sum([int(j) for j in str(i)]) == N:
        count = 1
        print(i)
        break

if count == 0:
    print(0)
