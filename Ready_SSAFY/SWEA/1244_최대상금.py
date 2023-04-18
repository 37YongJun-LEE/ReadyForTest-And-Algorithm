T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    card, change = map(list, input().split())

    card = [int(i) for i in card]
    change = int(change[0])

    print(max(card))

    print(card, change)



"""

3
123 1
2737 1
32888 2

"""