T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    line, password = tuple(input().split())

    line = int(line)
    password = list(password)

    answer_stack = []
    for i in password:
        answer_stack.append(i)
        if len(answer_stack) >= 2:
            if answer_stack[-1] == answer_stack[-2]:
                answer_stack.pop()
                answer_stack.pop()

    print('#' + str(test_case), "".join(answer_stack))

