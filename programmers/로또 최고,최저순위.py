def solution(lottos, win_nums):
    answer = []

    lowest = 0
    highest = 0

    for i in win_nums:
        if i in lottos:
            lowest += 1  # 당첨 번호가 몇 개인지 알면 그것이 최저 당첨순위
            lottos.remove(i)

    num = lottos.count(0)  # 0 몇 개 인지 세기

    highest = lowest+num

    dap = [highest, lowest]

    for j in dap:
        if j == 6:
            answer.append(1)
        elif j == 5:
            answer.append(2)
        elif j == 4:
            answer.append(3)
        elif j == 3:
            answer.append(4)
        elif j == 2:
            answer.append(5)
        else:
            answer.append(6)

    return answer
