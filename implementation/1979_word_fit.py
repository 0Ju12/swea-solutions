T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())

    board = []

    for _ in range(N):
        board.append(list(map(int, input().split())))

    answer = 0


    # =====================
    # 1. 가로 검사
    # =====================
    for row in board:
        cnt = 0

        for value in row:
            if value == 1:
                cnt += 1

            else:
                if cnt == K:
                    answer += 1

                cnt = 0

        if cnt == K:
            answer += 1


    # =====================
    # 2. 세로 검사
    # =====================

    for c in range(N):

        cnt = 0

        for r in range(N):

            # 현재 위치
            value = board[r][c]

            if value == 1:
                cnt += 1

            else:

                if cnt == K:
                    answer += 1

                cnt = 0


        # 마지막이 1로 끝나는 경우
        if cnt == K:
            answer += 1


    print(f"#{tc} {answer}")
