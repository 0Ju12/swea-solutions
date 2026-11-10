T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input().strip() for _ in range(N)]

    min_value = 999999

    for i in range(N - 2):
        for j in range(i + 1, N - 1):

            total = 0

            # 흰색 영역
            for r in range(0, i + 1):
                for c in range(M):
                    if arr[r][c] != 'W':
                        total += 1

            # 파란색 영역
            for r in range(i + 1, j + 1):
                for c in range(M):
                    if arr[r][c] != 'B':
                        total += 1

            # 빨간색 영역
            for r in range(j + 1, N):
                for c in range(M):
                    if arr[r][c] != 'R':
                        total += 1

            if total < min_value:
                min_value = total

    print(f'#{tc} {min_value}')
