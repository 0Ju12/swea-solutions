from collections import defaultdict
from math import factorial

T = int(input())

def dfs(count, left, right):
    global visited

    if dp[visited][left] > 0:
        return dp[visited][left] 

    if left >= (total_sum / 2):
        dp[visited][left] =  2**(N-count) * factorial(N-count)
        return  dp[visited][left]
    
    if count == N:
        return 1

    case_count = 0
    for i in range(N):
        if visited & (1 << i):
            continue

        visited |= (1<<i)
        case_count += dfs(count+1, left+weights[i], right)
        if left >= right+weights[i]:
            case_count += dfs(count+1, left, right+weights[i])
        visited ^= (1<<i)
    dp[visited][left] = case_count
    return dp[visited][left]
    

for tc in range(1, T + 1):
    N = int(input())
    weights = list(map(int, input().split()))
    total_sum = sum(weights)

    # dp[사용한 무게 추(visited)[left 무게추] = 경우의 수]
    dp = [defaultdict(int) for _ in range(1 << N)] # 비트 연산
    visited = 0

    answer = dfs(0,0,0)

    print(f"#{tc} {answer} ")
