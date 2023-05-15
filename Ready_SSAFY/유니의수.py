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
