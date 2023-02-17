# 정수를 저장하는 큐 구현, 입력으로 주어지는 명령 처리하는 프로그램 구현
import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()
for i in range(n):
    cmd = sys.stdin.readline().split()
    if len(cmd) == 2:   # push_back and push_front
        if cmd[0] == "push_front":
            queue.appendleft(cmd[1])
        elif cmd[0] == "push_back":
            queue.append(cmd[1])
    else:
        if cmd[0] == 'pop_front':
            try:
                print(queue[0])
                queue.popleft()
            except:
                print(-1)
        elif cmd[0] == 'pop_back':
            try:
                print(queue[-1])
                queue.pop()
            except:
                print(-1)
        elif cmd[0] == 'size':
            print(len(queue))
        elif cmd[0] == 'empty':
            if len(queue) == 0:
                print(1)
            else:
                print(0)
        elif cmd[0] == 'front':
                try:
                    print(queue[0])
                except:
                    print(-1)
        elif cmd[0] == 'back':
            try:
                print(queue[-1])
            except:
                print(-1)