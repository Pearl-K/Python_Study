import sys
input = sys.stdin.readline
s = input().rstrip()
num, alph = [], []
for i in range(len(s)):
    if s[i].isdigit():
        num.append(int(s[i]))
    else:
        alph.append(s[i])
numSum = str(sum(num))
alph.sort()
print(''.join(alph)+numSum)



