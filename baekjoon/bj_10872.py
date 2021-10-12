N = int(input())

def fact(n,answer):
    if n==0: return print(1)
    elif n==1:
        return print(answer)

    answer = answer*n
    n=n-1

    # 재귀호출
    fact(n,answer)

fact(N,1)

