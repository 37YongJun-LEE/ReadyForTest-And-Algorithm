# 정수를 저장하는 큐 구현, 입력으로 주어지는 명령 처리하는 프로그램 구현
import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()
for i in range(n):
    cmd = sys.stdin.readline().split()
    if len(cmd) == 2:   # push
        queue.append(cmd[1])
    else:
        if cmd[0] == 'pop':
            try:
                print(queue[0])
                queue.popleft()
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



# 명령 총 6가지

# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
