T = int(input())

def dfs(count):
    global answer

    if count == N :
        answer += 1
        return

    for c in range(N):
        # 열검사
        if c in col_visited:
            continue
        # 대각검사
        for r in range(count):
            if count-r == abs(c-pick_col[r]):
                #만약 대각 검사에 통과하지 못했다면
                break
            else:
                # 대각검사에 통과했다면
                col_visited.add(c)
                pick_col[count] = c
                dfs(count+1)
                col_visited.remove(c) 



for tc in range(1, T + 1):
    answer = 0
    N = int(input)
    pick_col = [-1] * N # dp[r] = c > 대각검사를 위함
    col_visited = set() # 열 검사를 위함
    dfs(0)

    print(f"#{tc} {answer}")
