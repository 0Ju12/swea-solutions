T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    carrots = list(map(int, input().split()))

    min_diff = 999
    answer = 0

    for i in range(1, N):
        left = sum(carrots[:i])
        right = sum(carrots[i:])

        diff = abs(left - right)

        if diff < min_diff:
            min_diff = diff
            answer = i

    print(f'#{tc} {answer} {min_diff}')
