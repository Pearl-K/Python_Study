import sys
import time
N, M = map(int, sys.stdin.readline().split())
cards = []
mins =[]
for i in range(N):
    cards.append(list(map(int, sys.stdin.readline().split())))
for j in range(N):
    mins.append(min(cards[j]))
print(max(mins))