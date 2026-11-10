for tc in range(1, 11):

    dump = int(input())
    box = list(map(int, input().split()))

    for _ in range(dump):

        box.sort(reverse=True)

        box[0] -= 1
        box[-1] += 1

    box.sort(reverse=True)

    result = box[0] - box[-1]

    print(f'#{tc} {result}')
