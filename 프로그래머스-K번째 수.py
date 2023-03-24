def solution(arr, commands):
    K = len(commands)
    ans = []

    for i in range(K):
        new = arr[commands[i][0] - 1: commands[i][1]]
        new.sort()
        ans.append(new[commands[i][2] - 1])

    return ans