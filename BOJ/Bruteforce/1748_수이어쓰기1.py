n = int(input())

num_len = []

num_len.append(0)
num_len.append(9)

k = len(str(n))

if k == 1:
    print(n)

# dp 테이블 사용
# l(i) = l(i-1) + (n - (10**(i-1) + 1) * len(n)
for i in range(2, k+1):
    num_len.append( num_len[i-1] + 9 * (10**(i-1))*i )

print( num_len[k-1] + (n - (10**(k-1)) + 1) * k )