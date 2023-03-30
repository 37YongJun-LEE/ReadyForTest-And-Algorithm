n, m = map(int, input().split())

coin = []
for i in range(n):
    coin.append(int(input()))

d = [10001] * (m+1) # m+1 개의 dp 저장공간 확보 & 10001로 나올 수 없는 값 만들어 저장
d[0] = 0

for i in range(n): # 화페 종류만큼 반복할것 2,3, 순서대로...
    for j in range(coin[i], m+1): # dp 테이블 만큼 반복해서 채우고 원하는값 만들어 놓기
        if d[j-coin[i]] != 10001:   #(j-coin[i])의 금액을 만드는 방법이 존재하는 경우에 실행
            d[j] = min(d[j], d[j-coin[i]]+1)


if d[m] == 10001:
    print(-1)
else:
    print(d[m])