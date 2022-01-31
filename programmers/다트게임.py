def solution(dartResult):
    answer = 0
    stack = []

    # 10은 두글자 숫자이므로 'a'로 대체해준다.
    dartResult = dartResult.replace('10', 'a')
    bonus = {'S': 1, 'D': 2, 'T': 3}

    for word in dartResult:
        if word.isdigit() or word == 'a':
            stack.append(10 if word == 'a' else int(word))
        elif word in bonus:
            # 바로 전 숫자 꺼내서 bonus만큼 제곱해주고 다시 저장
            num = stack.pop()
            stack.append(num ** bonus[word])
        elif word == '*':
            num = stack.pop()
            if len(stack):  # 하나 꺼내도 스택에 남아있는게 있으면
                stack[-1] *= 2  # 제일 마지막것에 제곱해서 넣기
            stack.append(num * 2)  # 해당 문자도 제곱해서 넣기
        elif word == '#':
            stack[-1] *= -1    # 마지막에 -1 곱하고 다시 넣기

    return sum(stack)  # 모든 처리된 값들 더해서 return
