N = int(input())
data = [1] * 10 # 2 ~ 9 진법일 경우의 유니수 저장할공간 마련
# 진법 변환하는 코드
for i in range(2, 10):
    now_decimal = i
    tmp = N
    answer = []
    while tmp > 0:
        answer.append(tmp % now_decimal)
        tmp = tmp // now_decimal

    for k in answer:
        if k == 0: continue
        data[i] *= k

max_decimal = 0
max_yuni = 0
for i in range(2, 10):
    if max_yuni <= data[i]:
        max_decimal = i
        max_yuni = data[i]
print( max_decimal, max_yuni)





"""
num = int(input())

data = [1] * 10

for k in range(2, 10):
    N = num
    answer = []
    while N > 0:
        answer.append(N % k)
        N = N // k
    for i in answer:
        if i == 0:
            continue
        data[k] *= i

yuni_num = 0
remain = 0
for i in range(2, 10):
    if yuni_num <= data[i]:
        yuni_num = data[i]
        remain = i

print(remain, yuni_num)
"""