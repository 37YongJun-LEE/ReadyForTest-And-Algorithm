N, M = map(int, input().split()) # 학생수 N, 비교수 M
student_height = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    student_height[b] += 1

for i in range(M+1):
    for j in range(1,N+1):
        if student_height[j] == i:
            print(j, end = ' ')

"""
N, M = map(int, input().split()) # 학생수 N, 비교수 M
student_height = {}

for i in range(1, N+1): # 학생 넘버와 value 저장
    student_height[i] = 0

for _ in range(M):
    a, b = map(int, input().split())
    student_height[b] += 1

answer = sorted(student_height.keys(), key = lambda x: student_height[x])

for k in answer:
    print(k, end = ' ')
"""


"""
################ 1
month_and_day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
week = ['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday' ]
M , D = map(int, input().split())
print(week[(sum(month_and_day[:M]) + D) % 7])

"""
"""
## template
                #0  1   2   3   4   5   6   7   8   9   10  11  12
month_and_day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
        # 나머지 0 , 1 .... 6
week = ['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday' ]
M , D = map(int, input().split())
print(week[(sum(month_and_day[:M]) + D) % 7])


"""