from itertools import combinations

# 소수 판별


def sosu(num):
    if num == 0 or num == 1:
        return False
    else:
        for n in range(2, (num//2)+1):
            if num % n == 0:
                return False
        return True


def solution(nums):
    answer = 0
    cmb = list(combinations(nums, 3))
    for i in cmb:
        if sosu(sum(i)):
            answer += 1
    return answer
