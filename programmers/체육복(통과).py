def solution(n, lost, reserve):
    # n: 전체 학생 수, lost: 도난당한 학생 번호, reserve: 여분있는 학생 번호
    # 여벌 체육복 가져온 학생도 도난 당했을 수 있다.

    answer = 0

    # 입을 수 있을지 검증해야 하는 애
    test = set(lost)-set(reserve)  # 2,4

    reserve_unif = set(reserve)-set(lost)  # 1,3,5

    for i in sorted(reserve_unif):  # 1,3,5
        if i-1 in test:
            test.remove(i-1)  # 이까 2뺏으니 없는거임!!!

        elif i+1 in test:
            test.remove(i+1)  # test에서 2빼기 #

    print(n-len(test))
