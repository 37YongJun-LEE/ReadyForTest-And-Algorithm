
"""
############ 정답풀이
n, m = map(int, input().split())
v = [[] for i in range(n + 1)]
cnt = [0 for i in range(n + 1)]
nodes = []
# 입력
for i in range(m):
  a, b = map(int, input().split())
  v[a].append(b)
  cnt[b] += 1

# 맨 앞에 올 수 있는 노드들을 nodes에 추가.
for i in range(1, n + 1):
  if cnt[i] == 0:
    nodes.append(i)
for i in range(n):
# 출력 가능한 노드 중 가장 작은 번호 찾기.
  x = nodes[0]
  idx = 0
for j in range(len(nodes)):
  if x > nodes[j]:
    x = nodes[j]
    idx = j
# 가장 작은 노드 출력 후 이 노드를 출력 가능 리스트에서 제거.
print(x, end=' ')
nodes.pop(idx)
# 출력한 노드에서 나가는 간선을 제거. 제거한 뒤 출력 가능해지는 노드를 출력 가능 리스트에 추가.
for j in v[x]:
  cnt[j] -= 1
if cnt[j] == 0:
  nodes.append(j)


"""

"""
N, M = map(int, input().split()) # 학생수 N, 비교수 M
student_height = {}

for i in range(1, N+1): # 학생 넘버와 value 저장
    student_height[i] = 0

for _ in range(M):
    a, b = map(int, input().split())
    student_height[b] += 1

answer = sorted(student_height.keys(), key = lambda x: student_height[x])

for k in answer:
    print(k, end = ' ')
"""


"""
################ 1
month_and_day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
week = ['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday' ]
M , D = map(int, input().split())
print(week[(sum(month_and_day[:M]) + D) % 7])

"""
"""
## template
                #0  1   2   3   4   5   6   7   8   9   10  11  12
month_and_day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
        # 나머지 0 , 1 .... 6
week = ['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday' ]
M , D = map(int, input().split())
print(week[(sum(month_and_day[:M]) + D) % 7])


"""