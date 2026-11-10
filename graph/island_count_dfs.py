T = int(input())
 
dr = [-1,1,0,0]
dc = [0,0,-1,1]
 
def dfs(x,y):
    WL_map[x][y]='W'
    for i in range(4):
        nr = x + dr[i]
        nc = y + dc[i]
        if nr>=N or nc>=M or nr<0 or nc<0:
            continue
        if WL_map[nr][nc]=='W':
            continue
        dfs(nr,nc)
 
 
 
for tc in range(1,T+1):
    N,M = map(int,input().split())
    WL_map = [list(input().strip()) for _ in range(N)]
    ans = 0
    for r in range(N):
        for c in range(M):
            if WL_map[r][c] =='L':
                ans+=1
                dfs(r,c)
    print(f'#{tc} {ans}')
