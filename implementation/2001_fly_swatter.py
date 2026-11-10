T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            total = 0

            for r in range(M):
                for c in range(M):
                    total += arr[i + r][j + c]

            answer = max(answer, total)

    print(f"#{test_case} {answer}")







# T = int(input())
 
# for tc in range(1, T+1):
#     answer = 0
 
#     N, M = map(int, input().split())
#     flies= [list(map(int, input().split())) for _ in range(N)]
 
#     # 1. 시작점 찾기
#     for start_r in range(N-M+1):
#         for start_c in range(N-M+1):
#             # 2. 시작점으로부터 M*M 돌면서 파리 잡기
#             temp_sum = 0
#             for dr in range(M):
#                 for dc in range(M):
#                     temp_sum += flies[start_r+dr][start_c+dc]
 
#             answer = max(answer, temp_sum)
 
#     print(f'#{tc} {answer}')
