month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
T = int(input())
for test_case in range(1, T+1):
    start_month, start_day, now_month, now_day = map(int, input().split())
    now_sum = sum(month[1:now_month]) + now_day
    start_sum = sum(month[1:start_month]) + start_day
    print('#{} {}'.format(test_case, now_sum - start_sum + 1))

"""
# 그냥 직관으로 푼 문제 -> 코드 보통
month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

T = int(input())
for test_case in range(1, T+1):
  start_month, start_day, now_month, now_day = map(int, input().split())
  the_day_before = 0
  if start_month == now_month:
      the_day_before = (now_day - start_day) + 1
  else:
      for i in range(start_month, now_month+1):
          if i == start_month: the_day_before += month[start_month] - start_day
          elif i == now_month: the_day_before += now_day
          else: the_day_before += month[i]
      the_day_before += 1
  print('#{} {}'.format(test_case, the_day_before)

"""