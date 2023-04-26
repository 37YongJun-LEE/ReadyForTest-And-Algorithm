T = int(input())
for test_case in range(1, T+1):
  N = int(input())
  data = list(map(int, input().split()))
  win = 0
  lose = 0
  for i in range(1,N):
    win_lose = data[i] - data[i-1]
    if win_lose >= 0:
      win = max(win, win_lose)
    else:
      lose = min(lose, win_lose)

  print(win, abs(lose))