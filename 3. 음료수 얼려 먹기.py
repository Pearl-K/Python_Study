N, M = map(int, input().split())
graph = []
#그래프 안에 입력
for i in range(N):
    a = list(map(int, input()))
    graph.append(a)

#dfs 함수
def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1 #방문 처리
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

res = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            res += 1

print(res)