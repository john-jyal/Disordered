#파이썬은 재귀 최대깊이를 늘려줘야한다... 런타임에러남
import sys
sys.setrecursionlimit(50000)


#주석인 부분이 더 느림 ( boolean 탐색이 빨라서인듯 )

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

testcase = int(input())


def DFS(x, y, farm):
    farm[y][x] += 1
# def DFS(x, y, farm, visited):
#     visited[y][x] = True

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny >= 0 and ny < n and nx >= 0 and nx < m and farm[ny][nx] == 1:
            DFS(nx, ny, farm)
    # for i in range(4):
    #     ny = y + dy[i]
    #     nx = x + dx[i]
    #     if ny >= 0 and ny < n and nx >= 0 and nx < m and not visited[ny][nx] and farm[ny][nx] == 1:
    #         DFS(nx, ny, farm, visited)


for tc in range(testcase):
    cnt = 0
    m, n, k = map(int, input().strip().split())
    farm = [[0] * m for _ in range(n)]
    # visited = [[False] * m for _ in range(n)]

    for i in range(k):
        x, y = map(int, input().strip().split())
        farm[y][x] = 1

    for y in range(n):
        for x in range(m):
            if farm[y][x] == 1  :
                DFS(x, y, farm)
            # if farm[y][x] == 1 and not visited[y][x] :
            #     DFS(x, y, farm, visited)
                cnt += 1

    print(cnt)
