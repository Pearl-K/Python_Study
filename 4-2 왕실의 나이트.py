pos = input()
alpha = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] #알파벳과 인덱스 1~8 대응

dx = [2, -2, 1, -1] #수평) 움직일 수 있는 경우의 수 list
dy = [1, -1, 2, -2] #수직) 움직일 수 있는 경우의 수 list

x, y = alpha.index(pos[0]), int(pos[1])
cnt = 0 #이동 가능 횟수를 세는 cnt

for i in range(2):
    for j in range(2):
        nx = x + dx[i]
        ny = y + dy[j]
        if nx >= 1 and nx <= 8 and ny >= 1 and ny <=8:
            cnt += 1

for i in range(2, 4):
    for j in range(2, 4):
        nx = x + dx[i]
        ny = y + dy[j]
        if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
            cnt += 1
print(cnt)