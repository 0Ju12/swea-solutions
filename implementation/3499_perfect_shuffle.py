T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cards = input().split()

    # 앞쪽 카드가 몇 장인지 계산
    mid = (N + 1) // 2

    # 카드 덱 두 부분으로 나누기
    first = cards[:mid]
    second = cards[mid:]

    result = []

    # 앞쪽 덱 기준으로 반복
    for i in range(len(first)):

        # 앞쪽 카드 먼저 추가
        result.append(first[i])

        # 뒤쪽에도 i번째 카드가 존재하는 경우만 추가
        if i < len(second):
            result.append(second[i])

    print(f'#{tc}', *result)
