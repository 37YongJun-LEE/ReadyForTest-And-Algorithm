T = int(input())
for test_case in range(1, T+1):
  N = int(input())
  cnt = 0
  for i in range(1,N+1):# i == A
    for j in range(1,N+1): # j == B
      if (j-i) * (j + i) == N:
        cnt += 1
  print('#{} {}'.format(test_case, cnt))