
# E <= 15
# S <= 28
# M <= 19


n, m, l = map(int, input().split())

E = 1
S = 1
M = 1

year = 1

while (n, m, l) != (E, S, M):
    E += 1
    if E == 16:
        E = 1

    S += 1
    if S == 29:
        S = 1

    M += 1
    if M == 20:
        M = 1

    year += 1


print(year)
