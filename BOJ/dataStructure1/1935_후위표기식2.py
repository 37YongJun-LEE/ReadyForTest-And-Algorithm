import sys

n = int(input())
quest = list(sys.stdin.readline().rstrip())

num_stack = []
for i in range(n):
    num_stack.append(int(sys.stdin.readline().rstrip()))

# 아마도 문제 포인트 --> ABC 순서랑 저장된 숫자 스택의 인덱스가 동일 하다.


cal_stack = []
idx = 0
for q in quest:
    cal = ''
    if q.isalpha():
        cal_stack.append(str(num_stack[idx]))
        if idx+1 < n:
            idx += 1
    else:
        b = cal_stack.pop()
        a = cal_stack.pop()
        cal = a+q+b
        cal_stack.append(cal)

answer = eval(cal)
print("{:.2f}".format(answer))






