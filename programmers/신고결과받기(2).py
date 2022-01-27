from collections import Counter


def solution(id_list, report, k):
    answer = []
    reported_dict = dict()  # 누가 누구를 신고했는지
    ban_cnt = []  # 신고 당한 내역

    for id in id_list:
        reported_dict.setdefault(id, [])

    for reported_id in report:
        a, b = reported_id.split()

        # 같은 신고는 1번만 저장
        if b not in reported_dict[a]:
            reported_dict[a].append(b)

            ban_cnt.append(b)

    # id별 신고당한 횟수 세기    #딕셔너리로 반환
    ban_dict = Counter(ban_cnt)

    # 파이썬스러운 한줄 코드
    for id in id_list:
        answer.append(
            len([check for check in reported_dict[id] if ban_dict[check] >= k]))

    return answer
