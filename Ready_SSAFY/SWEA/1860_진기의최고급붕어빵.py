# 전부 구현하려 하지 말고, 각 손님이 도착할 때마다. 현재 남은 빵 개수를 구하여,
# 빵 개수가 음수인지 아닌지만 판별하는 것이 포인트
# 한번이라도 못주는 경우 impossible 출력하게 하기.

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split()) # M초마다 K개씩 만듬

    arrive = list(map(int, input().split()))
    arrive.sort()
    #print('#{}번 {}초마다 {}개씩 만듬'.format(test_case, M, K))
    #print(arrive) # len(arrive) == N

    #남은 붕어빵 개수  ## timer가 M일때 마다 bread_cnt +K개 추가
    bread_cnt = 0

    # 가능 여부
    impossible = False

    prev = -1
    for i in range(N):
        # 이전 시간과 다른 경우에만 붕어빵 개수 추가.
        if prev != arrive[i]:
            # 손님 arrive[i]초에 도착 시, 붕어빵 개수
            bread_cnt = ((arrive[i] // M) * K) - i

            #print( '현재 {}초 붕어빵 {}개'.format(arrive[i], bread_cnt))
            prev = arrive[i]

        # 손님 붕어빵 주기 가능 여부
        if bread_cnt > 0:
            continue
        else:
            impossible = True
            #print(impossible)
            break
    if impossible:
        print('#{} Impossible'.format(test_case))
    else:
        print('#{} Possible'.format(test_case))



"""
4
74 60 97
59 60 60 61 60 60 61 59 60 61 60 59 59 59 60 61 61 60 60 59 60 61 59 61 61 60 60 60 59 60 60 59 59 61 60 59 61 59 61 59 59 61 60 61 61 59 60 59 59 59 61 60 59 59 59 59 60 60 61 61 61 60 59 59 61 59 61 61 59 59 60 59 61 61
46 66 6
10029 4659 3269 6238 277 6404 1754 1788 5109 2386 1814 10710 6247 10117 1149 4097 9301 6215 10399 1736 4805 2140 9517 3995 5596 6407 8259 3680 6476 1351 7811 5533 3863 1876 8345 10823 9466 8695 1553 1452 7425 2080 9585 1948 1213 4517
95 29 2
7051 3854 6810 8131 8561 5349 10987 5401 7911 2951 3929 10900 3375 3067 7248 5184 1216 2195 10107 3174 6029 483 1715 9712 166 9611 2048 9534 1670 1864 3616 4801 4512 1331 7307 9791 2757 1929 304 2579 5001 10113 4492 2087 2987 1438 10571 3558 8239 1169 5606 8707 3879 8903 5376 10619 2435 5517 3220 2611 1118 7452 7783 10214 10577 9491 1422 3520 5238 10975 8442 2564 10482 4277 10043 7905 2688 7893 9147 385 3122 5246 9657 971 9594 1581 2680 5065 9717 4683 3684 1828 5548 4664 558
33 33 81
34 33 34 32 34 34 34 34 34 34 34 34 32 33 34 32 34 34 34 32 34 32 32 34 33 32 32 34 34 32 33 33 34
"""

