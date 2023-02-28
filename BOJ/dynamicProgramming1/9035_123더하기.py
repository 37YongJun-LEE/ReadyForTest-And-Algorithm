# f(n) = f(n-1) + f(n-2) + f(n-3)
n = int(input())



for i in range(n):
    k = int(input())
    d = [0] * (k+3)     # 왜 k+3을 해줘야하는지 정확히 이해되지 않는다...
    d[1] = 1
    d[2] = 2
    d[3] = 4
    for j in range(4, k+1):
        d[j] = d[j-1] + d[j-2] + d[j-3]
    print(d[k])