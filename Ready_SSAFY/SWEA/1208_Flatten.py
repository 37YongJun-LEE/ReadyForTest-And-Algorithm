
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    dump_cnt = int(input())
    boxes = list(map(int, input().split()))

    for i in range(1, dump_cnt+1):
        boxes.sort()
        boxes[-1] -= 1
        boxes[0] += 1

    boxes.sort()
    print('#' + str(test_case), boxes[-1] - boxes[0])


    # ///////////////////////////////////////////////////////////////////////////////////
