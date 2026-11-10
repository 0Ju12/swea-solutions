# 12345 > '12345'
# a = input()
# print(a)

# 12345 > ['1', '2', '3', '4', '5']
# a = list(input())
# print(a)

# 12345 > [1, 2, 3, 4, 5]
# a = list(map(int, input()))
# print(a)

# 3   > N
# 123 
# 456
# 789
# [
#    ['1', '2', '3'],
#    ['4', '5', '6'],
#    ['7', '8', '9'],
# ]

# N = int(input())
# a = [list(input()) for _ in range(N)]
# print(a)

# 3   > N
# 123 
# 456
# 789
# [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9],
# ]

# N = int(input())
# a = [list(map(int, input())) for _ in range(3)]
# print(a)

# 3   > N
# 1 2 3 
# 4 5 6
# 7 8 9
# [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9],
# ]

# N = int(input())
# a = [list(map(int, input().split())) for _ in range(3)]
# print(a)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer90 = [[0] * N for _ in range(N)]

    for j in range(N):
        for i in range(N - 1, -1, -1):
            answer90[j][N - i - 1] = arr[i][j]

    answer180 = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            answer180[N - i - 1][N - j - 1] = arr[i][j]

    answer270 = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            answer270[N - j - 1][i] = arr[i][j]

    print(f'#{tc}')

    for i in range(N):
        print(
            ''.join(map(str, answer90[i])),
            ''.join(map(str, answer180[i])),
            ''.join(map(str, answer270[i]))
        )




# T = int(input())
# def turn_90(numbers):
#     result = [[0]*N for _ in range(N)]
#     for r in range(N):
#         for c in range(N):
#             result[r][c] = numbers[N-1-c][r]
#     return result


# for tc in range(1, T + 1):
#     N = int(input())
#     numbers = [input().split() for _ in range(N)]

#     numbers_90 = turn_90(numbers)
#     numbers_180 = turn_90(numbers_90)
#     numbers_270 = turn_90(numbers_180)

#     print(f'#{tc}')
#     for r in range(N):
#         print(''.join(numbers_90[r]),''.join(numbers_180[r]),''.join(numbers_270[r]))
