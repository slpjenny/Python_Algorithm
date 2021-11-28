def solution(n, lost, reserve):
    # n: 전체 학생 수, lost: 도난당한 학생 번호, reserve: 여분있는 학생 번호
    # 여벌 체육복 가져온 학생도 도난 당했을 수 있다.
    answer = 0

    min_student = n-len(lost)  # 1,3,5

    reserve_set = set()
    borrow_done = []

    for i in reserve:  # 3
        for j in lost:  # 2,4
            if i in borrow_done:
                continue

            elif i == j:
                min_student = min_student+1
                continue

            elif j in list(range(i-1, i+2, 1)):  # 2 in 2,3,4 #4 in 234
                reserve_set.add(j)  # 한번 빌려줬으면 끝! 중복으로 빌려주는게아님
                borrow_done.append(i)  # 3으로 2를 빌려줌

    answer = min_student + len(reserve_set)
    print(answer)

    return answer
