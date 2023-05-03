T = int(input())
for test_case in range(1, T + 1):
    flower = list(map(int, input().split()))
    answer = 1000000
    num = 1
    while True:
        cnt = 0
        for i in range(len(flower)):
            if num % flower[i] == 0:
                cnt += 1
        if cnt == 3: break
        num += 1
    print(num)