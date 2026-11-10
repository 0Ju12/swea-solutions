T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = input()

    answer = "NONE"

    for i in range(N - M + 1):
        word = arr[i:i + M]

        if word == word[::-1]:
            answer = word
            break

    print(f"#{tc} {answer}")
