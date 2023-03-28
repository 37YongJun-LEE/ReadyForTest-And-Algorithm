# 책 풀이
n = int(input())
array = list(map(int, input().split()))

d = [0] * 100

# dp 바텀업 진행
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])

    
print(d[n-1])


"""
# 내 풀이
    # 위와는 생각은 동일한데, 조금 다르다.
        # 어쩃든 홀수와 짝수에 영향이 안가게 계산할 수 있으니
        # 마지막에서 최대인 것을 구하면 되는 것 아닌가? -> 해서 이렇게 구성
        # 생각 했지만 이렇게 구성하면 안된다. 
        # 문제는 1칸 이상 띄라했지, 1칸만 띄라 하진 않았다.

import sys
n = int(input())

store = list(map(int, sys.stdin.readline().split()))
store += [0] * 2

for i in range(2, n+2):
    store[i] = store[i] + store[i-2]


print( max(store[-1], store[-2]))

"""


