T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    pw_count = int(input())
    pw = list(input().split())

    cmd_count = int(input())
    cmd = list(input().split())

    for i in range(len(cmd)):
        if cmd[i] == 'I':
            input_loc = int(cmd[i + 1])
            N = int(cmd[i + 2])
            insert_numbers = cmd[i + 3:i + 3 + N]

            for j in range(N):
                pw.insert(input_loc + j, insert_numbers[j])

        else:
            continue

    print('#' + str(test_case), " ".join(pw[0:10]))

