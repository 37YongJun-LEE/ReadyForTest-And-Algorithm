import sys
data = sys.stdin.readline().rstrip()

num = 0
alpha = list()

answer = []

for x in data:
    if x.isalpha():
        answer.append(x)
    else:
        num += int(x)
answer.append(str(num))

print("".join(answer))



"""
import sys

data = sys.stdin.readline().rstrip()

num = list()
alpha = list()

for i in data:
    try:
        a = int(i)
        num.append(a)
    except:
        alpha.append(i)

alpha.sort()
alpha = "".join(alpha)
print(alpha + str(sum(num)))
"""
"""K1KA5CB7

AJKDLSI412K4JSJ9D
"""