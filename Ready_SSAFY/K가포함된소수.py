def check(x, y): # x의 수에서 y가 있는지 여부
    while x > 0:
        if x % 10 == y: return True
        x = x // 10
    return False

# 에라스토테네스의 채
is_prime = [True] * (1000001)
is_prime[0] = False
is_prime[1] = False
prime = []

for i in range(2, 1000001):
    if not is_prime[i]: continue
    for j in range(i * i, 1000001, i):
        is_prime[j] = False

for i in range(1000001):
    if is_prime[i]: prime.append(i)

##########################
T = int(input())
for test_case in range(1, T+1):
    v, s, e = map(int, input().split())
    cnt = 0
    for i in range(len(prime)):
        if prime[i] < s: continue
        elif prime[i] > e: break
        if check(prime[i], v): cnt += 1

    print('#{} {}'.format(test_case, cnt))


# 이 문제에서 기억해야할 것

# 0. '에라토스테네스의 채'를 알고 있어야한다.
# 1. 입력받기 전에 미리 정해진 최대범위에서 모든 소수의 배열을 구한다 ( 각 테스트 케이스마다 구하는 것은 매우 비효율적이다 .
# 2. 입력 받은 다음 원하는 범위에서만 탐색을 진행한다.
# 3. 해당 탐색을 위한 함수를 따로 만들어 관리한다. ( 편의성 )
# 4. check 함수로 (%10) 시간효율성을 확보한다. ( str로 찾지 않기 )
