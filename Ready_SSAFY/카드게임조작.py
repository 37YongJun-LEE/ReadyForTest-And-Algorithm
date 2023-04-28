T = int(input())
for test_case in range(1, T+1):
  data = list(map(int, input()))
  sum = 0   # 현재까지 카드합
  ans = 0   # 추가된 카드 수
  for i in range(len(data)):
    if data[i] > 0:
      if sum + ans < i:
        ans += i - (sum + ans)
    sum += data[i]
  print('#{} {}'.format(test_case, ans))

"""
10
210100212
1021022221
10012
212221
22022222
1101002
0001200002
0002
1100111
2122102

"""