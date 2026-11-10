T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    day, month, quarter, answer = map(int, input().split())
    plan = list(map(int, input().split()))

    dp = [0]*13  # dp[i] = i월까지의 최소 비용, dp[0] = 0
    for i in range(1,13):
        #0: 일권을 썻을 때
        #1: 월권을 썻을 때
        #2: 3개월권을 썼을때
        fees = [day*plan[i-1], month, float('inf')]

        # 첫달이 아닐 때만 이전달에 대해 누적 처리
        if i > 0:
            fees[0] += dp[i-1]
            fees[1] += dp[i-1]

        # 3개월권은 1~2월에 사도 그 달까지 덮음
        fees[2] = quarter + dp[max(0, i-3)]
  
        dp[i] = min(fees)
    
    answer = min(dp[12], answer)

    print(f"#{tc} {answer} ")
