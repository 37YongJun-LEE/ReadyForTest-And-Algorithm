import sys
import time
start_time = time.time()

# push, pop, size, empty, top
n = int(sys.stdin.readline())

stack = []
for i in range(n):
    data = sys.stdin.readline().split()
    cmd = data[0]

    if cmd == 'push':
        stack.append(data[1])
    elif cmd == 'pop':
        try:
            print(stack[-1])
            stack.pop()
        except:
            print(-1)
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif cmd == 'top':
        try:
            print(stack[-1])
        except:
            print(-1)

end_time = time.time()
print("time: ", end_time - start_time)


