T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    day, month, quarter, answer = map(int, input().split())
    plan = list(map(int, input().split()))

    dp = [0]*12
    for i in range(1,13):
        #0: 일권을 썻을 때
        #1: 월권을 썻을 때
        #2: 3개월권을 썼을때
        fees = [day*plan[i], month, float('inf')]

        # 첫달이 아닐 때만 이전달에 대해 누적 처리
        if i > 0:
            fees[0] += dp[i-1]
            fees[1] += dp[i-1]

        if i >= 2:
            fees[2] = quarter
            if i>=3:
                fees[2] += dp[i-3]
  
        dp[i] = min(fees)
    
    answer = min(dp[11], answer)

    print(f"#{tc} {answer} ")
