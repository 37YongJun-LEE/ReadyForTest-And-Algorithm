import sys

n, m = map(int, sys.stdin.readline().split())
rice_cake = list(map(int, sys.stdin.readline().split()))

rice_cake.sort()
#print(rice_cake)
start = 0
end = rice_cake[-1]

while start <= end:
    sum = 0
    mid = (start + end) // 2
    #print(mid)

    # mid로 다 자른다음 결과보기
    for R in rice_cake:
        if R > mid:
            sum += (R-mid)
        else:
            continue

    # sum과 m 비교
    if sum < m:
        end = mid - 1
    else:   # 일치할 때가 아니라, 최디한 덜 잘랐을때가 답, 따라서 result를 따로 만들어 기록
        result = mid
        start = mid + 1

print(result)





