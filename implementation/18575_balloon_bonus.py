T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_score = -float('inf')
    min_score = float('inf')

    for i in range(N):
        for j in range(N):
            total = 0

            for k in range(N):
                total += arr[k][j]

            for k in range(N):
                total += arr[i][k]

            total -= arr[i][j]

            if total > max_score:
                max_score = total

            if total < min_score:
                min_score = total

    answer = max_score - min_score

    print(f'#{tc} {answer}')
