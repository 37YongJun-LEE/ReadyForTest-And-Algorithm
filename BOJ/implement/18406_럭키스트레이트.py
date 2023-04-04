import sys

num = list(map(int, input()))



k = len(num)//2

print(num[:k], num[k:])

if sum(num[:k]) == sum(num[k:]):
    print("LUCKY")
else:
    print("READY")