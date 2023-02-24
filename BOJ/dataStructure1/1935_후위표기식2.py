n = int(input())

quest = list(str(input()))

num_stack = [ int(input()) for _ in range(n)]

stack = []
for i in quest:
    if i.isalpha():
        number = ord(i) - ord('A')
        stack.append(num_stack[number])

    else:
        b = stack.pop()
        a = stack.pop()
        if i == "+":
            stack.append(a+b)

        elif i == "-":
            stack.append(a-b)

        elif i == "*":
            stack.append(a*b)

        elif i == "/":
            stack.append(a/b)

print("%.2f" %stack[0])