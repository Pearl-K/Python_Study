from collections import deque
N, M = map(int, input().split())
graph = []
#그래프 안에 입력
for i in range(N):
    a = list(map(int, input()))
    graph.append(a)

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    if 0 <= x and x < N and 0 <= y and y < M and graph[x][y] == 0:
        queue = deque()
        queue.append((x, y))
        graph[x][y] = 1

        while True:
            if not queue:
                return 1
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                #공간을 벗어난 경우 무시
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                if graph[nx][ny] == 0:
                    queue.append((nx, ny))
                    graph[nx][ny] = 1
        return 1
    else:
        return 0

res = 0
for i in range(N):
    for j in range(M):
        res += bfs(i, j)
print(res)