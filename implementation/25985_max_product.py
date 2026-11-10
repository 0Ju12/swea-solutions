T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_total = -999999999

    # A를 기준으로 B와 겹칠 수 있는 모든 위치 확인
    for shift in range(-(N - 1), M):

        total = 0

        for i in range(N):
            j = i + shift

            # 실제로 겹치는 부분만 계산
            if 0 <= j < M:
                total += A[i] * B[j]

        if total > max_total:
            max_total = total

    print(f'#{tc} {max_total}')
