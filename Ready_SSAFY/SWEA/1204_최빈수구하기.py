# 점수 dp 를 이용해서 테이블 생성후 max일때의 i를 출력하자


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    dp = [0] * 101

    task_num = int(input())
    student_score = list(map(int, input().split()))

    for score in student_score:
        dp[score] += 1

    prev = 0
    for i in range(len(dp)):
        if prev <= dp[i]:
            prev = dp[i]
            answer = i

    print('#' + str(task_num), answer)

    # ///////////////////////////////////////////////////////////////////////////////////


