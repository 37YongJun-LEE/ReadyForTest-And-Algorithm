money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    print('#{} '.format(test_case))
    for i in money:
        answer = N // i
        print(answer, end = ' ')
        N = N % i
    print()

# 간단한 원리이지만, 경험해보지 못한 문제면 어려울수 있는 문제, 
# 다른 거스름돈 문제의 경우에도 큰 단위로 나눈 경우에 남는 몫과 나머지를 이용해서 답을 도출할 수 있다. 
# 전형적인 그리디 문제
"""
2 
32850
160             
 
"""

