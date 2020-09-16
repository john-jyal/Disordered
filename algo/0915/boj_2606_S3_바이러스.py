def DFS(cur, graph, visited):
    visited[cur] = 1
    for i in range(len(graph[cur])):
        if graph[cur][i] == True and visited[i] == 0:
            DFS(i, graph, visited)


computer = int(input()) + 1
link = int(input())

graph = [[0] * computer for i in range(computer)]

for i in range(link):
    info = list(map(int,input().split()))
    start = info[0]
    end = info[1]

    graph[start][end] = 1
    graph[end][start] = 1

visited = [0] * computer

DFS(1, graph, visited)
cnt = 0
for i in range(len(visited)):
    if(visited[i] == 1):
        cnt += 1

print(cnt-1)