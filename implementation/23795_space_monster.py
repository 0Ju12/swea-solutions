#1
#5
#0 0 0 1 0
#1 0 1 1 0
#0 0 1 0 2
#1 0 0 0 0
#1 1 1 1 0

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 괴물 위치 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                r = i
                c = j

    # 위
    for i in range(r - 1, -1, -1):
        if arr[i][c] == 1:
            break
        arr[i][c] = 2

    # 아래
    for i in range(r + 1, N):
        if arr[i][c] == 1:
            break
        arr[i][c] = 2

    # 왼쪽
    for j in range(c - 1, -1, -1):
        if arr[r][j] == 1:
            break
        arr[r][j] = 2

    # 오른쪽
    for j in range(c + 1, N):
        if arr[r][j] == 1:
            break
        arr[r][j] = 2

    # 안전한 0 개수
    answer = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                answer += 1

    print(f'#{tc} {answer}')
