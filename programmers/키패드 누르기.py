def solution(numbers, hand):
    answer = ''

    L = [1, 4, 7]
    R = [3, 6, 9]

    num_dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
               4: [1, 0], 5: [1, 1], 6: [1, 2],
               7: [2, 0], 8: [2, 1], 9: [2, 2],
               '*': [3, 0], 0: [3, 1], '#': [3, 2]}

    # 시작 위치
    left_s = num_dic['*']
    right_s = num_dic['#']

    for i in numbers:
        # now = 지금 누르려고 하는 번호 위치
        now = num_dic[i]

        if i in L:
            answer += 'L'
            left_s = now
        elif i in R:
            answer += 'R'
            right_s = now

        # 2,5,8,0 누르는 경우
        else:
            left_d = 0
            right_d = 0

            for a, b, c in zip(left_s, right_s, now):
                left_d += abs(a-c)
                right_d += abs(b-c)

            if left_d < right_d:
                answer = answer + 'L'
                left_s = now

            elif left_d > right_d:
                answer = answer + 'R'
                right_s = now

            # 두 거리가 같은 경우
            else:
                if hand == 'left':
                    answer = answer + 'L'
                    left_s = now

                elif hand == 'right':
                    answer = answer + 'R'
                    right_s = now

    return answer
