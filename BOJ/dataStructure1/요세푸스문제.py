import sys

n, k = map(int, sys.stdin.readline().split())

circle = list()
for i in range(1, n+1):
    circle.append(i)

answer = []

start = 0
while circle:
    if len(circle) < k:
        pop_idx = (k-1) - len(circle)
    else:
        pop_idx = start + (k - 1)

    while pop_idx >= len(circle):
        pop_idx = pop_idx - len(circle)

    answer.append(circle[pop_idx])
    circle.pop(pop_idx)
    start = pop_idx

    print(circle)
    print(start)
    print(answer)
    print("-------------------")

print("<"+str(answer).strip("[]") + ">")

