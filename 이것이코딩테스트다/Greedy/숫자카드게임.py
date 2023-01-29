n, m = map(int, input().split())

# 먼저 뽑고자 하는 가드의 행을 선택 ( 가로 )
# 그다음 선택 행에서 가장 낮은 숫자 뽑기
min_list = []

for i in range(n):
    data = list(map(int, input().split()))
    minimum = min(data)
    min_list.append(minimum)

print(max(min_list))
