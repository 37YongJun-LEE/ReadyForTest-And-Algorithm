T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    data = list(map(int, input()))
    answer = 0
    if data[0] == 1:
        answer += 1
    for i in range(1,len(data)):
        #print(data[i-1], data[i])
        if data[i-1] != data[i]:
            answer += 1
        else:
            continue
    print('#{} {}'.format(test_case, answer))

"""
for i in range(1,4):
    print(i-1, i)
"""


