T = int(input())
coin = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for test_case in range(1, T+1):
  N = int(input())
  answer = []
  for i in coin:
    answer.append(N // i)
    N = N % i
  print(answer)

