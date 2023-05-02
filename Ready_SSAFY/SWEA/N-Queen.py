

"""month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

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
print(the_day_before)
"""