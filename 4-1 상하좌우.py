import sys
input = sys.stdin.readline

N = int(input())
plan = list(input().split())
start = [1, 1] #start[0]은 왼쪽 좌표, start[1]은 오른쪽 좌표
now = start

for i in plan:
    if i == 'L':
        if now[1] == 1: #더 이상 왼쪽으로 갈 수 없는 상태
            continue
        else:
            now[1] -= 1
    elif i == 'R':
        if now[1] == 5: #더 이상 오른쪽으로 갈 수 없는 상태
            continue
        else:
            now[1] += 1
    elif i == 'U':
        if now[0] == 1: #더 이상 위로 갈 수 없는 상태
            continue
        else:
            now[0] -= 1
    else: #D일 때
        if now[0] == 5: #더 이상 내려갈 수 없는 상태
            continue
        else:
            now[0] += 1

print(*now)