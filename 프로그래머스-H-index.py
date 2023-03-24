def solution(citations):
    citations.sort()
    N = len(citations)
    res = []

    for i in range(N):
        h = N - i
        if citations[i] >= h:
            res.append(h)
    if res:
        ans = res[0]
    else:
        ans = 0

    return ans