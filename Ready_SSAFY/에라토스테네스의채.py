N = int(input())
is_prime = [True] * (N+1)
is_prime[0] = False
is_prime[1] = False

for i in range(2, N+1):
    if not is_prime: continue

    for j in range(i*i, N+1, i):
        is_prime[j] = False

for i in range(N+1):
    if is_prime[i]: print(i, end=' ')