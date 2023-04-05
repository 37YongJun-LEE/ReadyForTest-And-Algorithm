import math
from itertools import permutations


def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    result_list = []
    numbers = list(numbers)

    for i in range(1, len(numbers) + 1):
        data = set(permutations(numbers, i))
        for d in data:
            prime = int("".join(d))
            if prime > 1:
                result_list.append(prime)

    result_list = list(set(result_list))

    for k in result_list:
        if is_prime_number(k):
            answer += 1

    return answer