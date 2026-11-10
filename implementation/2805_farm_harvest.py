T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    farm = []

    for _ in range(N):
        farm.append(list(map(int, input())))

    total = 0
    center = N // 2

    for i in range(N):
        for j in range(N):
            if abs(i - center) + abs(j - center) <= center:
                total += farm[i][j]

    print(f"#{test_case} {total}")

# N은 홀수

# T = int(input())

# for tc in range(1,T+1):
#     answer = 0
#     N = int(input())
#     crops = [input() for _ in range[N]]

#     mid = distance = N  //2 

#     for r in range(N):
#         for c in range (abs(mid-r), N-2*(abs(mid-r)+abs(mid-r))): # 시작점을 땡겨주는 역할
#             answer += int(crops[r][c]) 

#     print(f'#{tc} {answer}' )
