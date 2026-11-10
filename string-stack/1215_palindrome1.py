for test_case in range(1, 11):
    N = int(input())
    square = []

    for _ in range(8):
        square.append(list(input()))

    sum = 0
    for i in range(8):
        for j in range(8 - N + 1):
            a = square[i][j:j+N]
            if a == list(reversed(a)):
                sum += 1

    for i in range(8 - N + 1):
        for j in range(8):
            b = [square[i+k][j] for k in range(N)]
            if b == list(reversed(b)):
                sum += 1

    print(f"#{test_case} {sum}")
