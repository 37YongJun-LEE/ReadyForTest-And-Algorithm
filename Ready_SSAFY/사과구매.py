T = int(input())
for test_case in range(1, T+1):
  data = list(map(int, input().split()))
  answer = []
  length = len(data)
  for i in range(length):
    for j in range(length):
      if i == j: break
      for k in range(length):
        if j == k or i == k: break
        answer.append(data[i] + data[j] + data[k])
  answer.sort()
  print('#{} {}'.format(test_case, answer[-5]))
