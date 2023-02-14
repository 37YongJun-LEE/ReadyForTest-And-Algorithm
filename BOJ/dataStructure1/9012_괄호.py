import sys

n = int(sys.stdin.readline())

for i in range(n):
    stack = []
    vps = sys.stdin.readline()

    for v in vps:
        if v == "(":
            stack.append(v)
        elif v == ")":
            try:
                if stack[-1] == "(":
                    stack.pop()
            except:
                stack.append(v)
    if len(stack) > 0:
        print("NO")
    else:
        print("YES")
