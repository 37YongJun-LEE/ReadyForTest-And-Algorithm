### 2번문항 replay

N = int(input())
data = list(map(int, input().split()))

v = [] # 짝수 넣어주기 리스트
for i in range(N):
    if data[i] % 2 == 0:
        v.append(i) # 짝수의 인덱스를 v 리스트에 넣어주어라
                    # 따라서 해당 위치만 순서대로 나올 수 있게 세팅

x = 0  # 0 1 0 1 0 1 .... 0 1
for i in range(len(v)):
    x += abs(v[i] - (2 * i))   # 0 2 4 6 ...

y = 0  # 1 0 1 0 1 0 .... 1 0
for i in range(len(v)):
    y += abs(v[i] - (2*i+1))


if N % 2 == 1: # 길이가 홀수인 경우
    if len(v) > N - len(v): # 짝수개수가 홀수보다 더 많은 경우
        y = x
    else:   # 홀수개수가 짝수보다 더 많은 경우
        x = y

answer = min(x, y)
print(answer)








################ 2번문항 : 물건진열
"""
n = int(input())
arr = list(map(int, input().split()))

v = []
for i in range(n):
  if arr[i] % 2 == 0:
    v.append(i)

x = 0
for i in range(len(v)):
  x += abs(v[i] - 2 * i)

y = 0
for i in range(len(v)):
  y += abs(v[i] - (2 * i + 1))

if n % 2 == 1:
  if len(v) > n - len(v):
    y = x
  else:
    x = y
print(min(x, y))

"""


############ 1번 문항
"""
# 0 ~ 9 까지 번호의 손가락
finger = [0] * 8
typing = { '1':0, 'q':0, 'a':0, 'z':0,
           '2': 1, 'w': 1, 's': 1, 'x': 1,
           '3': 2, 'e': 2, 'd': 2, 'c': 2,
           '4': 3, 'r': 3, 'f': 3, 'v': 3,
           '5': 3, 't': 3, 'g': 3, 'b': 3,

           '6': 4, 'y': 4, 'h': 4, 'n': 4,
           '7': 4, 'u': 4, 'j': 4, 'm': 4,
           '8': 5, 'i': 5, 'k': 5, ',': 5,
           '9': 6, 'o': 6, 'l': 6, '.': 6,
           '0': 7, 'p': 7, ';': 7, '/': 7,
           '-': 7, '[': 7, "'": 7, '=': 7, ']': 7
           }
word = input()
for w in word:
    finger[ typing[w] ] += 1
for i in finger:
    print(i, end = ' ')
"""

