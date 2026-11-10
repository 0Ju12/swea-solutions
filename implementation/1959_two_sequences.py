T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    a_arr = list(map(int, input().split()))
    b_arr = list(map(int, input().split()))

    if N > M:
        N, M = M, N
        a_arr, b_arr = b_arr, a_arr

    max_total = 0

    for shift in range(M - N + 1):
        total = 0

        for i in range(N):
            total += a_arr[i] * b_arr[i + shift]

        max_total = max(max_total, total)

    print(f'#{tc} {max_total}')
