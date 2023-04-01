n = int(input())
data = list(map(int, input().split()))

count = 0
data.sort()

while True:
    n = n - data[-1]
    count += 1
    data.pop()

    if data[-1] <= n:
        count += 1
        break

print(count)


"""
# 2023/04/01 풀이
import sys

n = int(input())

people = list(map(int, sys.stdin.readline().split()))

people.sort()       # 맨 마지막 사람이 가장 무서움을 많이 느끼는 사람

cnt = 0
while people:
    k = people.pop()
    cnt += 1
    for i in range(k-1):
        if not people:
            break
        people.pop()

print(cnt)

"""


"""
# 책 정답 풀이

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0
        
print(result)
"""
