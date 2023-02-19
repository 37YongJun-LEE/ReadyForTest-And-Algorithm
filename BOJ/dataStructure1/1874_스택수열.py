import sys
from collections import deque

n = int(input())
target_queue = deque()
stack = []

for i in range(n):
    k = int(sys.stdin.readline())
    target_queue.append(k)

answer_list = []
count = 0

for i in range(1, n+1):
    stack.append(i)
    answer_list.append('+')
    while True:
        if len(target_queue) == 0 or len(stack) == 0:
            break
        if stack[-1] == target_queue[count]:
            stack.pop()
            target_queue.popleft()
            answer_list.append('-')
        else:
            break

if answer_list.count('+') != answer_list.count('-'):
    print('NO')
else:
    for a in answer_list:
        print(a)
    
