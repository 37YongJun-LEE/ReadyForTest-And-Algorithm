import sys
from collections import deque

input_queue = deque(sys.stdin.readline().rstrip())
stack = []  # 답 print를 위한 스택
reverse_stack = [] # stack에 리버스 해서 넣기 위한 임시 스택

while input_queue:
    if input_queue[0] == "<":
        if len(reverse_stack) > 0:  #  2,3,4 ...n번째 "<" 만난 경우
            stack.append("".join(reverse_stack[::-1]))
            reverse_stack = []

        while input_queue[0] != ">":
            stack.append(input_queue[0])
            input_queue.popleft()
        # 마지막 ">" 담기
        stack.append(input_queue[0])
        input_queue.popleft()

    else:
        # " ", "<" 만나면 리버스 스택에 있는 애들을 역순으로 바꾸어 stack에 넣은 다음, " "또는 "<" 도 stack에 넣기
        if input_queue[0] == " ":  #
            stack.append("".join(reverse_stack[::-1]))
            reverse_stack = []
            stack.append(input_queue[0])
            input_queue.popleft()

        # 리버스 스택에 넣기
        else:
            reverse_stack.append(input_queue[0])
            input_queue.popleft()
        # " " 이거나 "<" 일때까지 리버스 스택에 넣기
if len(reverse_stack) > 0:
    stack.append("".join(reverse_stack[::-1]))

print("".join(stack))