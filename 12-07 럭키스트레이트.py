import sys
input = sys.stdin.readline
N = input().rstrip()
length = len(N)
left, right = 0, 0
for i in range(length//2):
    left += int(N[i])
    right += int(N[-1-i])

if left == right:
    print("LUCKY")
else:
    print("READY")