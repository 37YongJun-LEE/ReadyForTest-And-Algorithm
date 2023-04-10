n = int(input())

math_problem = input()

stack = []
for i in math_problem:
    if i.isnumeric():
        stack.append(int(i))


