# N=동전의 종류 개수, K=값
N, K = map(int, input().split())

# N개의 줄에 동전의 가치가 오름차순으로 주어진다.
A_list = []
total_coin = 0

for i in range(N):
    A_list.append(int(input()))


for a in reversed(A_list):

    if K == 0:
        break

    if a > K:  # 왜 얘의 존재 유무가 영향을끼치지?
        continue

    coin_num = K//a  # 나눈 몫을 집어넣는다.
    total_coin += coin_num

    K -= a*coin_num


print(total_coin)
