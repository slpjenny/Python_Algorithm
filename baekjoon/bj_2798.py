# N :카드의 개수
# M: M과 가장 가까운 수를 만들어야함

# N장의 카드 중에서 3장의 카드를 골라야 한다.

N,M = map(int,input().split())
card = list(map(int,input().split()))

num = []
remove_num = []

for i in range(N):
    for j in range(i+1,N,1):
        for k in range(j+1,N,1):
            if card[i]+card[j]+card[k] > M :
                continue
            else:
                num.append(card[i]+card[j]+card[k])

print(max(num))
                








