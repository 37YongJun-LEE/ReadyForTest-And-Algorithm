import sys

n = int(input())
coin = list(map(int, sys.stdin.readline().split()))

coin.sort()

# 문제해결 아이디어
    # 화페단위를 기준으로 오름차순 정렬하여 
    # 1부터 target-1까지의 모든 금액을 만들 수 있는지를 확인하는 코드를 작성하면 된다
    # 금액을 만들 수 있다면, target를 업데이트 해주면 된다
    # 
    # 화폐단위를 기준으로 정렬한 뒤에, 화폐단위가 작은 동전부터 하나씩 확인하면서
    # target 변수를 업데이트 하는 방법으로 문제를 풀 수 있다...
    
target = 1
for x in coin:
    if target < x:  # 1 이후로 목표로하는 다음 타겟 금액보다 X의 금액이 크면 target는 만들 수 없는 수이다.
        break
    target += x

print(target)