# 주어진 문제의 입력조건이 1이상 100000 이하이므로 그저 라이브러리 사용해도 무방
# 이름과 점수가 있으므로 2차원 배열로 만들어 key=점수로 정렬하는 것이 효과적
# 성적 낮은 순으로 학생 이름만 출력


n = int(input())

grade = []
for i in range(n):
    name, score = input().split()
    grade.append([name, int(score)]) # 다음부턴 튜플을 이용해보자

sorted(grade, key = lambda x : x[1])

print(grade)

for i in grade:
    print(i[0], end = ' ')