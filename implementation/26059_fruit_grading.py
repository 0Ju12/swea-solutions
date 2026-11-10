T = int(input())

for tc in range(1, T + 1):
    N, lo, hi = map(int, input().split())
    fruits = list(map(int, input().split()))

    # 1. 무게 순서대로 정렬
    fruits.sort()

    answer = 999999

    # 첫 번째 경계
    # Economy 개수 = i
    for i in range(1, N):

        # 같은 무게 사이에서는 K1을 둘 수 없음
        if fruits[i - 1] == fruits[i]:
            continue

        # Economy 개수가 lo~hi 범위인지 검사
        economy = i

        if not (lo <= economy <= hi):
            continue

        # 두 번째 경계
        for j in range(i + 1, N):

            # 같은 무게 사이에서는 K2를 둘 수 없음
            if fruits[j - 1] == fruits[j]:
                continue

            standard = j - i
            premium = N - j

            # 세 등급 모두 lo 이상 hi 이하인지 확인
            if (
                lo <= economy <= hi
                and lo <= standard <= hi
                and lo <= premium <= hi
            ):

                max_cnt = max(economy, standard, premium)
                min_cnt = min(economy, standard, premium)

                diff = max_cnt - min_cnt

                answer = min(answer, diff)

    if answer == 999999:
        answer = -1
    print(f'#{tc} {answer}')
