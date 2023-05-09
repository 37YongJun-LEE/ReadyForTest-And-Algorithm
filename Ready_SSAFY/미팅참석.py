# well known 문제 : 끝나는 시간이 가장 빠른 순으로 정렬하여,
# 앞에서부터 차례대로 조건에 맞는 미팅을 참석해 나아가는 것이 최대개수를 가질 수 있다.
N = int(input())
data = []
for i in range(N):
    start, end = map(int, input().split())
    data.append((start, end))
# 이거 대신에 처음부터 저장을 (end, start)순으로 저장하면 sort() lambda 안써도 정렬 가능하다.
data.sort(key= lambda x: x[1])
cut_line = 0
cnt = 0
for start, end in data:
    if cut_line <= start:
        cut_line = end
        cnt += 1
    else:
        continue
print(cnt)