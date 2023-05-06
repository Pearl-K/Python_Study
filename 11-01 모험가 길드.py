import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
cnt, num = 0, 1

for i in range(N):
    if arr[i] <= num:
        cnt += 1
        num = 1
    else:
        num += 1

print(cnt)