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
                # 대각 검사에서 걸리면 이 열은 못 씀
                break
        else:
            # 모든 이전 행과 대각이 겹치지 않을 때만 (for-else)
            col_visited.add(c)
            pick_col[count] = c
            dfs(count+1)
            col_visited.remove(c) 



for tc in range(1, T + 1):
    answer = 0
    N = int(input())
    pick_col = [-1] * N # dp[r] = c > 대각검사를 위함
    col_visited = set() # 열 검사를 위함
    dfs(0)

    print(f"#{tc} {answer}")
