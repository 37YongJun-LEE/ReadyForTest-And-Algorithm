
N = int(input())
is_prime = [True] * (1000000)  # 전부 소수라고 가정하고 시작
is_prime[0] = False
is_prime[1] = False  # False 인 경우 소수인데, 1은 거르기 위해서 처리
prime = []

for i in range(2, N + 1):
    if not is_prime[i]: continue
    for j in range(i*i, N + 1, i):  # 해당 수의 배수는 전부 False 처리 따라서 해당 수가 소수.
        is_prime[j] = False
for i in range(2, N + 1):
    if is_prime[i]: prime.append(i)

cnt = 0
for i in range(len(prime)):
    for j in range(len(prime)):
        for l in range(len(prime)):
            if i + j + l == N: cnt += 1
