from math import factorial

T = int(input())

def dfs(count, left, right):
    global answer 

    if left >= (total_sum / 2):
        answer += 2**(N-count) * factorial(N-count)
        return

    if count == N :
        answer += 1
        return
    
    for i in range(N):
        if visited[i]:
            continue

        visited[i] = 1
        dfs(count+1, left+weights[i], right)
        if left >= right+weights[i] :
            dfs(count+1, left, right+weights[i])

        visited[i] = 0

for tc in range(1, T + 1):
    answer = 0
    
    N = int(input())
    weights = list(map(int, input().split()))
    visited = [0]*N
    total_sum = sum(weights)

    dfs(0, 0, 0)

    print(f"#{tc} {answer} ")
