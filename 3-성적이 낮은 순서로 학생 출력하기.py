import sys
input = sys.stdin.readline
N = int(input())
students = []
for i in range(N):
    name, grade = input().split()
    students.append((name, int(grade)))

students.sort(key=lambda x: x[1])

for i in range(N):
    print(students[i][0], end=' ')
