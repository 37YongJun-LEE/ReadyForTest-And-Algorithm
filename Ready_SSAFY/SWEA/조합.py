# 페르마의 소정리를 알아야지 풀 수 있는 문제, 대회 나갈거 아니면 몰라도 될듯

"""
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, R = map(int, input().split())

    up = 1
    down = 1
    for i in range(R):
        up *= N-i
        down *= R-i
    answer = (up // down) % 1234567891

    print('#{} {}'.format(test_case, int(answer) ))
"""