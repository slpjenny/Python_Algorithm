def solution(answers):
    # 1번 수포자 : (1~5)반복
    # 2번 수포자: 21 -> 23 -> 24-> 25
    # 3번 수포자: (33 11 22 44 55) 반복

    # 동점이면 모두 리턴
    # ------------------------------

    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0]  # 수포자들의 총점수(맞은점수 세기)
    result = []  # 결과값 리스트

    for idx, answer in enumerate(answers):  # idx =0,1,2   answer = 정답 순서대로 나열
        if answer == supo1[idx % len(supo1)]:  # 나머지는 0,1,2,...
            score[0] += 1  # 해당 수포자의 점수 올라감
        if answer == supo2[idx % len(supo2)]:
            score[1] += 1
        if answer == supo3[idx % len(supo3)]:
            score[2] += 1

    for idx, s in enumerate(score):  # 점수를 하나씩 꺼내서
        if s == max(score):  # 그게 셋 중 가장 큰 점수이면
            result.append(idx+1)  # 해당 수포자 번호를 결과값 리스트에 추가

    return result
