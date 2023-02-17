n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort() #수 정렬
first = data[n-1] #가장 큰 수
second = data[n-2] # 두 번째로 큰 수

#가장 큰 수_first 가 더해지는 횟수 계산
count = int(m/(k+1))*k
count += m%(k+1)

result = 0
result += count * first #가장 큰 수 더하기 계산
result += (m-count) * second #두 번째로 큰 수 더하기 계산
print(result)