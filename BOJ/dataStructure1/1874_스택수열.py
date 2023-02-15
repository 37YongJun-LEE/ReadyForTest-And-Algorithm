import sys
import time

start_time = time.time()
n = int(sys.stdin.readline())
target_stack = []
stack = []
answer = []

for i in range(n):
    k = int(sys.stdin.readline())
    target_stack.append(k)

count = 0
for i in range(1, n+1):
    if target_stack[count] > i:
        stack.append(i)
        answer.append("+")
        continue
    elif target_stack[count] == i:
        stack.append(i)
        answer.append("+")
        try:
            while stack[-1] == target_stack[count]:
                stack.pop()
                answer.append("-")
                count += 1
        except:
            break
if len(answer) == n*2:
    for k in answer:
        print(k)
else:
    print("NO")
    
end_time = time.time()
print(end_time-start_time)