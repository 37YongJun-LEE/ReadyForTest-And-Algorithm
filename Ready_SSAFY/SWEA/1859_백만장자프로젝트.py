# 최댓값 갱신을 거꾸로 계산하면 나온다는 아이디어... 아이디어만 나오면 매우 쉬운 문제였다...
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    price_per_day = list(map(int, input().split()))
    max_price = 0
    answer  = 0

    for i in range(N-1, -1, -1): # idx 거꾸로 순
        #print(price_per_day[i], max_price)
        #print('--------------------')
        if price_per_day[i] > max_price:
            max_price = price_per_day[i]
            continue
        answer += max_price - price_per_day[i]
    print(answer)






"""
3
3
10 7 6
3
3 5 9
5
1 1 3 1 2

1
5
1 1 3 1 2

"""



"""
4
2
522 4575
5
6426 9445 8772 81 3447
10
629 3497 7202 7775 4325 3982 4784 8417 2156 1932
50
5902 5728 8537 3857 739 6918 9211 9679 8506 3340 6568 1868 16 7940 6263 4593 1449 6991 310 3355 7068 1431 8580 1757 9218 4934 4328 3676 9355 6221 9080 5922 1545 8511 4067 5467 8674 4691 6504 9835 2034 4965 9980 1221 5895 2501 8152 8325 7731 9302

"""