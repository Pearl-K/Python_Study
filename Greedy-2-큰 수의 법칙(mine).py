import sys
N, M, K = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num.sort(reverse=True)
result, cnt = 0, 0
while True: #while 문 하나만 쓰고 나머지는 계산
    result += (num[0] * K)
    M -= K
    if M < K:
        cnt = 1
        break
    result += num[1]
    M -= 1
    if M < K:
        cnt = 2
        break
if cnt == 1:
    result += num[1]
    M -= 1
    for i in range(M):
        result += num[0]
else:
    result += num[0]*M

print(result)
