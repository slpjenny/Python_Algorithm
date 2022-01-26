def solution(id_list, report, k):
    answer = []
    id_dict = dict()
    name_count = dict()
    ban_id = []
    e_answer = 0

    for ids in id_list:
        id_dict.setdefault(ids, [])
        name_count.setdefault(ids, 0)

    for reported in report:
        a, b = reported.split()

        # 같은 ID 신고는 1번으로 처리
        if b not in id_dict[a]:
            # 누가 누굴 신고했는지 저장 딕셔너리 id_dict
            id_dict[a].append(b)

    # 신고를 몇번 당했는지 저장 딕셔너리 name_count
    for i in id_dict.values():
        for j in i:
            if j in name_count:
                name_count[j] += 1

    # k번 이상 신고당한 ID들 ban_id에 저장
    for c in name_count:
        if name_count[c] >= k:
            ban_id.append(c)

    for d in id_dict.values():
        for e in d:
            if e in ban_id:
                e_answer += 1
        answer.append(e_answer)
        e_answer = 0

    return answer
