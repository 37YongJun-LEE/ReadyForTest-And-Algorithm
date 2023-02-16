import sys

n = int(sys.stdin.readline().rstrip())
cmd = sys.stdin.readline().split()
print(cmd)



gps = [1,1]

for LRUD in cmd:
    if LRUD == "L" and 1 < gps[1] <= n:
        gps[1] -= 1

    elif LRUD == "R" and 1 <= gps[1] <= n:
        gps[1] += 1

    elif LRUD == "U" and 1 < gps[0] <= n:
        gps[0] -= 1

    elif LRUD == "D" and 1 <= gps[0] < n:
        gps[0] += 1

print(gps)