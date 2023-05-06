import sys
input = sys.stdin.readline
S = input()
result = 0
for i in range(len(S)-1):
    if i == 0:
        result = int(S[i])
    elif S[i] == '0':
        result += int(S[i])
    elif result == 0:
        result += int(S[i])
    else:
        result *= int(S[i])
print(result)