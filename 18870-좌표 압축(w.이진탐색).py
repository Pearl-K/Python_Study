N = int(input())
X = list(map(int, input().split()))
newX = list(set(X))
newX.sort()

def BinarySearch(arr, target):
    mid = len(arr) // 2
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

res = []
for i in range(N):
    idx = BinarySearch(newX, X[i])
    res.append(idx)

print(*res, end=' ')