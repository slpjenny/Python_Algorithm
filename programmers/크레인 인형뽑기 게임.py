def solution(board, moves):
    answer = 0  # 터트려져 사라진 인형의 개수
    index = 0
    new_board_list = []  # 새 일차원 배열
    new_board = []  # 새 이차원 배열
    baguni = []

    for i in range(len(board)):
        for j in board:
            if j[index] == 0:   # 0뺀 리스트로 새로운 이차배열 만들기
                continue
            else:
                new_board_list.append(j[index])

        new_board.append(new_board_list)
        new_board_list = []
        index += 1

    for move in moves:  # [1,5,3,5,1,2,1,4]
        if new_board[move-1]:
            baguni.append(new_board[move-1].pop(0))

        else:
            continue

        # 같은 모양 인형이 두개 쌓이면 사라진다.
        if len(baguni) >= 2 and baguni[-1] == baguni[-2]:
            baguni.pop()
            baguni.pop()

            answer += 2

    return answer
