# for _ in range(10):
#     tc, E = map(int, input().split())
#     arr = list(map(int, input().split()))

#     graph = [[] for _ in range(100)]

#     for i in range(0, len(arr), 2):
#         start = arr[i]
#         end = arr[i + 1]
#         graph[start].append(end)

#     visited = [0] * 100
#     result = 0

#     def dfs(node):
#         global result

#         if node == 99:
#             result = 1
#             return

#         visited[node] = 1

#         for next_node in graph[node]:
#             if visited[next_node] == 0:
#                 dfs(next_node)

#     dfs(0)

#     print(f"#{tc} {result}")

from collections import defaultdict


T = 10

def dfs(node):
    global answer
    visited[node] = 1

    if node == 99:
        answer = 1
        return

    for next_node in adj_list[node]:
        if visited[next_node]:
            continue

        dfs(next_node)



    
for tc in range(1, T+10):
    answer = 0
    _, M = map(int, input().split())
    load_info = list(map(int, input().split()))

    adj_list = defaultdict(list)
    visited = [0]*100
    for i in range(0, len(load_info), 2):
        adj_list[load_info[i]].append(load_info[i+1])
        # 양방향일경우
        # adj_list[load_info[i+1]].append(load_info[i])

    dfs(0)
         

    print(f'#{tc} {answer} ')
