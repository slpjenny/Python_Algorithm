def solution(new_id):
    answer = ''

    # 1단계
    new_id = new_id.lower()

    # 2단계
    # 가능한 특수문자 제외 모두 삭제
    # 알파벳 소문자,숫자 제외 모두 삭제
    remain = ['-', '_', '.']
    new_id = ''.join(char for char in new_id if char.isalnum()
                     or char in remain)

    # 3단계 (중복X,연속문자인 마침표 제거)
    stack = []
    for c in new_id:
        if c == '.':  # 마침표인 경우만 아래 알고리즘 적용
            if len(stack) == 0:
                stack.append(c)
            else:
                if c == stack[-1]:
                    continue
                else:
                    stack.append(c)
        else:
            stack.append(c)
    new_id = stack

    # 4단계
    if new_id[0] == '.':
        if len(new_id) >= 2:
            new_id = new_id[1:]
        else:
            new_id = '.'

    if new_id[-1] == '.':
        new_id = new_id[:-1]

    new_id = list(new_id)
    # 5단계
    if len(new_id) == 0:
        new_id.append('a')

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[0:15]
        if new_id[-1] == '.':
            new_id.pop()

    # 7단계
    if len(new_id) <= 2:
        while(len(new_id) < 3):
            new_id.append(new_id[-1])

    return ''.join(new_id)
