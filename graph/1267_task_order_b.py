from collections import deque
 
def bfs():
    q = deque()
 
    for i in range(1, len(task_count)):
        if task_count[i] == 0:
            q.append(i)
 
    while q:
        cur_node = q.popleft()
        print(cur_node, end=' ')
 
        for next_node in adj_list[cur_node]:
            task_count[next_node] -= 1
 
            if task_count[next_node] <= 0:
                q.append(next_node)
 
T = 10
 
for tc in range(1, T+1):
    V, E = map(int, input().split())
    info = list(map(int, input().split()))
 
    adj_list = [[] for _ in range(V+1)]
    task_count = [0]*(V+1)
 
    for i in range(0, E*2, 2):
        a, b = info[i], info[i+1]
        adj_list[a].append(b)
        task_count[b] += 1
 
    print(f'#{tc}', end=' ')
    bfs()
    print()
