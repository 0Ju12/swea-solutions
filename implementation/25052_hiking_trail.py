T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = 0

    for i in range(N):
        for j in range(N):

            r = i
            c = j
            length = 1

            while True:
                min_value = arr[r][c]
                next_r = -1
                next_c = -1

                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]

                    if 0 <= nr < N and 0 <= nc < N:
                        if arr[nr][nc] < min_value:
                            min_value = arr[nr][nc]
                            next_r = nr
                            next_c = nc

                if next_r == -1:
                    break

                r = next_r
                c = next_c
                length += 1

            if length > answer:
                answer = length

    print(f'#{tc} {answer}')
