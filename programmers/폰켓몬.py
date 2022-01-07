def solution(nums):
    answer = 0
    take = len(nums)/2

    nums = set(nums)  # 중복 종류 제거

    if take < len(nums):
        answer = take
    else:
        answer = len(nums)

    return answer
