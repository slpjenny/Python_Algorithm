def solution(N, stages):
    result = {}
    length = len(stages)

    for i in range(1, N+1):
        # 해당 스테이지에 머물러있는 사람 수 세기

        if length != 0:
            num = stages.count(i)
            # 실패율 구하기
            fail = num / length
            result[i] = fail

            length = length - num

        else:
            result[i] = 0

            # values 기준으로 key 출력
    return sorted(result, key=lambda x: result[x], reverse=True)
