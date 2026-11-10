T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr1 = [-1, 1, 0, 0]
    dc1 = [0, 0, -1, 1]

    dr2 = [-1, -1, 1, 1]
    dc2 = [-1, 1, -1, 1]

    max_value = 0

    # 모든 칸을 중심으로 확인
    for r in range(N):
        for c in range(N):

            # 중심 칸은 먼저 포함
            plus_total = arr[r][c]
            x_total = arr[r][c]

            # + 모양 계산
            for d in range(4):

                # 중심 포함 M칸이므로
                # 중심 제외하고 1 ~ M-1 이동
                for k in range(1, M):

                    nr = r + dr1[d] * k
                    nc = c + dc1[d] * k

                    if 0 <= nr < N and 0 <= nc < N:
                        plus_total += arr[nr][nc]

            # x 모양 계산
            for d in range(4):

                for k in range(1, M):

                    nr = r + dr2[d] * k
                    nc = c + dc2[d] * k

                    if 0 <= nr < N and 0 <= nc < N:
                        x_total += arr[nr][nc]

            max_value = max(max_value, plus_total, x_total)

    print(f'#{tc} {max_value}')
