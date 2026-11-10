from collections import deque

for test_case in range(1, 11):
    V, E = map(int, input().split())
    data = list(map(int, input().split()))

    graph = [[] for _ in range(V + 1)]
    indegree = [0] * (V + 1)

    for i in range(0, E * 2, 2):
        start = data[i]
        end = data[i + 1]

        graph[start].append(end)
        indegree[end] += 1

    q = deque()

    for i in range(1, V + 1):
        if indegree[i] == 0:
            q.append(i)

    result = []

    while q:
        current = q.popleft()
        result.append(current)

        for next_node in graph[current]:
            indegree[next_node] -= 1

            if indegree[next_node] == 0:
                q.append(next_node)

    print(f"#{test_case}", *result)
