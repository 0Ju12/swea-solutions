T = int(input())

for tc in range(1, T+1):
    N = int(input())
    heights = list(map(int, input().split()))

    max_height = max(heights)
    one_count = two_count = 0

    for height in heights:
        diff_height = max_height-height
        two_count += diff_height // 2
        one_count += diff_height % 2
    while two_count-one_count > 1:
        two_count -= 1
        one_count += 2

    if two_count >= one_count:
        answer = two_count*2
    else:
        answer = one_count*2-1

    print(f'#{tc} {answer}')
