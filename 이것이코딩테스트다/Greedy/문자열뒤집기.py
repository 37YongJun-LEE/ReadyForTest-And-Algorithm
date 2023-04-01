import sys

number = sys.stdin.readline().rstrip()

one_count = 0
zero_count = 0

Front = int(number[0])
if Front == 1:
    one_count += 1
else:
    zero_count += 1


for i in range(1, len(number)):
    Rear = int(number[i])

    if Front != Rear:
        Front = Rear
        if Front == 1:
            one_count += 1
        else:
            zero_count += 1

    else:
        Front = Rear

if (one_count + zero_count) == 1:
    print(0)
else:
    print(min(one_count, zero_count))


