def solution(num):
    count = 0

    if num == 1:
        return 0  # 단 주어진수가 1이면 0을 리턴

    while (num != 1):
        if num % 2 == 0:
            num = num // 2  # 짝수면  // 2
            count += 1

        elif num % 2 == 1:
            num = num * 3 + 1  # 홀수면 *3 + 1
            count += 1

        if count >= 500:
            return -1
            break
        # 작업을 500번 이상 반복하면 -1 리턴

    return count