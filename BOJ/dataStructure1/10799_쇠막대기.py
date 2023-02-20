import sys

stick_lazer = sys.stdin.readline()
stick_lazer = stick_lazer.replace("()", "1")

# count_1 쓰는거 회의적 굳이 스택에 있는데 셀필요 있나?
# 잘리는 개수는 세야하니 필요하긴 할듯

stack = []
count_1 = 0
piece_count = 0

for s in stick_lazer:
    stack.append(s)
    if s == ")":
        while True:
            if stack[-1] == "(":
                stack.pop()   # pop()해서 "(" 나올때 까지 없애기
                break
            elif stack[-1] == "1":
                count_1 += 1
            stack.pop()

        piece_count += count_1 + 1    # 잘리는 막대 개수 구하기
        for _ in range(count_1):
            stack.append("1")   # 같이 빠진 1 복구
        count_1 = 0 # count_1 초기화

print(piece_count)



