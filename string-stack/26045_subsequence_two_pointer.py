T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    b_idx = 0

    for i in range(N):

        if b_idx < M and A[i] == B[b_idx]:
            b_idx += 1

    if b_idx == M:
        answer = 'YES'
    else:
        answer = 'NO'

    print(f'#{tc} {answer}')
