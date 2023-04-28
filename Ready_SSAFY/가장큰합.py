T = int(input())
for test_case in range(1, T+1):
  N, M = map(int, input().split())
  data = list(map(int, input().split()))
  answer = 0
  for i in range(N):
    for j in range(i, N):
      if j == i: continue
      if data[i] + data[j] <= M: answer = max(answer, data[i]+data[j])
  if answer == 0: answer = -1
  print('#{} {}'.format(test_case, answer))