def solution(sizes):
    answer = 0
    widths = []   # 두 개의 모서리 중 큰 값을 가로
    heights = []   # 작은 값을 세로 라고 한다.

    for i in sizes:
        widths.append(max(i))
        heights.append(min(i))

    answer = max(widths)*max(heights)

    return answer
